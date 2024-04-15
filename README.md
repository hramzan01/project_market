# Project Market: Solar Energy Management Platform

## Description
Market is a cutting-edge solar energy management app designed to optimize cost savings through advanced data analytics and predictive modeling. By leveraging energy demand, usage, and price models, Market empowers users to make informed decisions about their energy consumption and investment in solar technologies.

![Market](https://raw.githubusercontent.com/hramzan01/project_market/master/app/assets/market_what.png)

### Key Features:
- **Solar Energy Management**: Market specializes in solar energy management, utilizing energy demand, usage, and price models to predict optimum cost savings.

- **Machine Learning and Deep Neural Network Technology**: Leveraging advanced machine learning and deep neural network technology, Market offers sophisticated analysis and predictions for efficient solar energy management.


## Project Directory
```bash
+---app
|   |   00_home.py
|   |   home.py
|   |   README.md
|   |
|   +---assets
|   |       logo.png
|   |       pzero_code.mp4
|   |       pzer_t2.mp4
|   |       pz_vid.mp4
|   |       pz_what.png
|   |
|   \---pages
|           01_utilities.py
|           02_carbon.py
|           03_population.py
|
+---config
|       file_renamer.py
|       pipeline.drawio
|       timeline.html
|
+---etl
|   |   carbon.py
|   |   extract.py
|   |   load.py
|   |   population.py
|   |   typologies.py
|   |   utilities.py
|   |   utils.py
|   |   __init__.py
|
+---notebooks
|       nb_carbon.ipynb
|       nb_data_merge.ipynb
|       nb_openai.ipynb
|       nb_population.ipynb
|       nb_sklearn_setup.ipynb
|       nb_sklearn_test_train.ipynb
|       nb_sus_coefficient.ipynb
|       nb_sus_targets.ipynb
|       nb_timeline.ipynb
|       nb_typologies.ipynb
|       nb_utilities_01.ipynb
|       nb_utilities_02.ipynb
|       nb_utilities_03.ipynb
|       nb_utilities_04.ipynb
|       nb_utilities_pipe.ipynb
|
+---pipeline
|       pipeline.pkl
|       pipeline.py
|       __init__.py
|
+---tests
|   |   test_pipeline.py
|   |   __init__.py
|
\---watchdog
        data_coefficients.csv
        data_demmand.csv
        data_design.csv
        data_population.csv
        energy_demmand.csv
        pipeline.pkl
        watchdog_monitor.py
```

## Getting Started

### Executing program
To start using Project Market, simply download the latest version from the repository and follow the installation instructions in the documentation.

### Dependencies
```bash
pip install -r requirements.txt
```

### Installing
```bash
pip install project_market
```

## Authors
- Haaris Ramzan, Le Wagon
- Adam Oxley, Le Wagon
- Rahul Iyer, Le Wagon
- Freddie Oxland, Le Wagon

## License
This project is licensed under MIT License - see the LICENSE.md file for details

## Acknowledgments
* The support of TA's and Staff at Le Wagon LDN Data Science and AI Batch #1461

---


