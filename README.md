# Roundface
Generate profile photos for all faces in a given image

## Requirements:
- Python 3
- OpenCV
- NumPy

## Setup
- Clone repo
- *CD* in project
- Create python virtual environment: `python -m venv venv`
- Activate virtual environment: `venv/bin/activate` or `venv\Scripts\activate`
- Install requirements with pip: `pip install -r requirement.txt`

## Usage:

`python roundface.py - s <path to image file or folder>`

## More Options:

*-g* or *--grey*  **Integer. 1 or 0. Specifies whether resulting photos should be greyed out.**

*- sz* or *--size*  **Integer. Desired output size in pixels**

*- r* or *--radius* **Integer (Float). e.g 1.2 for 20% more than the default radius.**

*Caution:* **Images must be able to accomodate space requirements (height and width) otherwise an exception will be thrown**


## Examples:

```
python roundface.py -s z://home/photos
python roundface.py -s z://home/photos/myself.jpg
python roundface.py -s vacation/photos - sz 400 -g 1
python roundface.py -s vacation/photos - sz 400 -r 1.0
```
## Credits:
[Pexels](https://www.pexels.com/)
[Towards Data Science](https://towardsdatascience.com/extracting-faces-using-opencv-face-detection-neural-network-475c5cd0c260)