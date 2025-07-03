# Flask_WebApp
# 🌆 City Scape - Procedural 2D/3D Map Generator

![City Scape Banner](github.com/kshitijdalvi4/Flask_CityMaps/blob/main/Generated_City.jpg)

**City Scape** is a powerful tool that generates game-ready 2D maps with geographical topology and converts them into 3D-ready JSON contour data for game developers.

## ✨ Features

- **Topology Selection**: Generate maps based on terrain type (Plains, Hills, Coastal)
- **2D Map Generation**: Automatically creates detailed 2D terrain maps
- **Image Processing**: Pre-processes maps for clean conversion
- **JSON Export**: Outputs elevation contours in game-ready JSON format
- **3D Integration**: Easy import into Unity, Unreal, or custom engines

## 🖼️ Examples

### 1. Generated 2D Maps
![Plains Map](image-url/plains.png) | ![Hills Map](image-url/hills.png) | ![Coastal Map](image-url/coastal.png)
---|---|---

### 2. JSON Contour Output
```json
{
  "metadata": {
    "mapType": "hills",
    "size": [1024, 1024]
  },
  "contours": [
    {"elevation": 0, "points": [[x1,y1], [x2,y2], ...]},
    {"elevation": 50, "points": [[x1,y1], [x2,y2], ...]}
  ]
}
