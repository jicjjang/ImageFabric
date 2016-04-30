ImageFabric
===
If you want **new image** by black &amp; white image, should be use this program.

## Image color to binary
white: RGB (255,255,255) => L (255) => 1

black: RGB (0,0,0) => L (0) => 0


##Installation
```sh
$ git clone https://github.com/jicjjang/ImageFabric.git
```


## How to use

##### if you not have **Pillow** library, you can first
```sh
$ pip install Pillow
```

##### Parameter
| Name        | Type   | Required | Description                                       |
|  ---        |  ---   | ---      |  ---                                              |
| filepath    | String | Yes      | image input path                                  |
| min_width   | int    | No       | (When the image crop) left point.                 |
| max_width   | int    | No       | (When the image crop) right point.                |
| min_height  | int    | No       | (When the image crop) top point.                  |
| max_height  | int    | No       | (When the image crop) bottom point.               |
| savepath    | String | No       | (If you specify the image path) image save path.  |

##### Example
```python
from fabric import Fabric
Fabric("IMG_PATH/IMAGE.PNG", 0, 0, 100, 100, 'IMG_SAVE_PATH/')\
    .create_saved_binary_to_image()
```

---
