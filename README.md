# io_anim_heavy_iron_studios
A Blender Addon for importing ANIM files by Heavy Iron Studios.

## Information for Users

This addon can only import animations, not models.

For model import, please use [DragonFF](https://github.com/Parik27/DragonFF) by Parik27.

### Features

- [x] Import animations
- [x] Multiple import possible
- [ ] Export animations (I'm working on it)

### Known Bugs

- Before you import an animation, make sure you have reset Rotation and Location of every bone in Pose Mode. You do this by selecting all bones in pose mode and pressing Alt+R and Alt+G

### Installation

You probably know how to install an Addon in Blender but in case you do not, here is a short Guide:

1. Download the latest ZIP-archive from the Releases
2. Open Blender (3.0.0 or above)
3. Menu Bar -> _Edit_ -> _Preferences_ -> _Add-ons_ -> _Install..._
4. Select the ZIP-archive and click on _Install Add-on_

## Information for Developers

### Architechture

_IMAGE HERE_

### Licensing

- The project used as a blender addon will be licensed as **GPLv3**
- The source code of AnimSKB.py, AnimSKBHeader.py, AnimSKBKey.py and Reader.py are **MIT licensed**

## Tested situations

| Platform | TSSM | BFBB |
| -------- | :--: | :--: |
| PS2      | yes  |  no  |
| Xbox     |  no  |  no  |
| GameCube |  no  |  no  |

**Note:** You can inform me about untested but working combinations, so I can update this table.

## Used resources

Thanks to the Modding Community for providing the structure of Heavy Iron Studios' ANIM files (https://heavyironmodding.org/wiki/ANIM)

And thanks to Seil for the [BFBBAnimTools](https://github.com/seilweiss/BFBBAnimTools) I used for understanding how to read the animation data (https://github.com/seilweiss/BFBBAnimTools/blob/master/BFBBAnimTools.ms)