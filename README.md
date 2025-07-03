# 🌆 City Scape - Procedural 2D/3D Map Generator

![City Scape Banner](https://raw.githubusercontent.com/kshitijdalvi4/Flask_CityMaps/main/Hero_Page.jpg)

**City Scape** is a powerful tool that generates game-ready 2D maps with geographical topology and converts them into 3D-ready JSON contour data for game developers.

## ✨ Features

- **Topology Selection**: Generate maps based on terrain type (Plains, Hills, Coastal)
- **2D Map Generation**: Automatically creates detailed 2D terrain maps  
  ![2D City](https://raw.githubusercontent.com/kshitijdalvi4/Flask_CityMaps/main/Generated_City.jpg)
- **Image Processing**: Pre-processes maps for clean conversion  
  ![Preprocessing](https://raw.githubusercontent.com/kshitijdalvi4/Flask_CityMaps/main/Preprocess.jpg)
- **JSON Export**: Outputs elevation contours in game-ready JSON format  
  ![JSON](https://raw.githubusercontent.com/kshitijdalvi4/Flask_CityMaps/main/JSON_img.jpg)
- **3D Integration**: Easy import into Unity, Unreal, or custom engines  
  ![3D City](https://raw.githubusercontent.com/kshitijdalvi4/Flask_CityMaps/main/3D.jpg)

## 🖼️ Examples

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
