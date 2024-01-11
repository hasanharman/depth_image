
# Zoe Depth Estimation

A brief description of what this project does and who it's for


## Usage/Examples

```bash
usage: cli.py [-h] input_image output_image

Depth estimation using ZoeDepth

positional arguments:
  input_image   Path to input image
  output_image  Path to output image

optional arguments:
  -h, --help    show this help message and exit
```


## Installation

Install depth estimation project with pip

```bash
  pip install -r requirements.txt
```
    
## Deployment

To deploy this project run

```bash
  docker build -t depth_estimation
  docker run -d -p 8041:8041 depth_estimation
```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## License

[MIT](https://choosealicense.com/licenses/mit/)

