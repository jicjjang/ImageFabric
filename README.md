ImageFabric
===
If you want **new image** by black & white image, should be use this program.

## Image color to binary
white: RGB (255,255,255) => L (255) => 1

black: RGB (0,0,0) => L (0) => 0


##Installation
```sh
$ git clone https://github.com/jicjjang/ImageFabric.git
```


##How to use

##### if you not have **Pillow** library, you can first
```sh
$ pip install Pillow
```

```python
from fabric import Fabric
fabric = Fabric("IMG_PATH/IMAGE.PNG")
fabric.create_saved_binary_to_image()
```