import os
os.environ['DYLD_FALLBACK_LIBRARY_PATH'] = '/opt/homebrew/lib'

import numpy as np
from dataclasses import dataclass
from tqdm import tqdm
from PIL import Image #for resizing images
from matplotlib import pyplot as plt
import shapely
import json
from rasterio.features import rasterize
import openslide as osl

@dataclass
class Tile:
    image_data:np.ndarray
    mask:np.ndarray
    x:int
    y:int

def get_mask(polygon:shapely.Polygon, bounds:tuple[int, int, int, int])->np.ndarray:

    minx, miny, maxx, maxy = bounds

    width = int(maxx - minx)
    height = int(maxy - miny)

    mask = np.zeros((height, width), dtype=np.uint8)

    shapes = [(polygon, 1)]
    rasterize(shapes, out=mask, transform=(1, 0, minx, 0, -1, maxy))

    return mask

def generate_tile(slide:osl.OpenSlide, shape:tuple[int, int], pos:tuple[int, int], mask_polygons:list[list[shapely.Polygon]])->Tile:
    width, height = shape
    x, y = pos

    # Get section of slide for region
    region = slide.read_region((x, y), 0, (width, height))
    region = region.convert('RGB')
    region_np = np.array(region)
    region_np = region_np.transpose((2, 0, 1))

    region_box = shapely.Polygon([[x, y], [x+width, y], [x+width, y+height], [x, y+height], [x, y]])

    mask = np.zeros((len(mask_polygons), width, height))

    for i, polygons in enumerate(mask_polygons):
        for j, polygon in enumerate(polygons[:-1]):
            if polygon.intersects(region_box):
                k = polygon.intersection(region_box)
                mask[i] += get_mask(k, (x, y, x+width, y+height))

    mask[mask >= 1] = 1
    return Tile(region_np, mask, x, y)

def get_mask_polygons(filename:str)->list[list[shapely.Polygon]]:
    with open(filename) as f:
        json_list = json.load(f)
    
    coordinates = []

    for j in json_list:
        if j['properties']['classification']['name'] == 'UDH-sure':
            coordinates.append(j['geometry']['coordinates'])

    output = []

    for i in range(len(coordinates)):
        for j in range(len(coordinates[i])):
            output.append(shapely.Polygon(coordinates[i][j]))

    return [output]




   

