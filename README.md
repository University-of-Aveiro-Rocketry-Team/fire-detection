## Fire Modules

The YOLOv8 modules used were trained by [@AlimTleuliyev](https://github.com/AlimTleuliyev) and are taken from the repository [https://github.com/AlimTleuliyev/wildfire-detection/tree/main](https://github.com/AlimTleuliyev/wildfire-detection/tree/main)

The modules are available in four sizes: fire_n, fire_s, fire_m, fire_l

### Licence

- [https://raw.githubusercontent.com/AlimTleuliyev/wildfire-detection/refs/heads/main/LICENSE](https://raw.githubusercontent.com/AlimTleuliyev/wildfire-detection/refs/heads/main/LICENSE)
- [LICENCE](fire-models/LICENSE)

## Setup

1. Download the YOLOv8 modules using the fire-modules.sh script

```bash
./fire-modules.sh [fire_n, fire_s, fire_m, fire_l]
```

2. Create a virtual environment and install the required packages

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```