# Project Market: Solar Energy Management Platform

## Description
Market is a cutting-edge solar energy management app designed to optimize cost savings through advanced data analytics and predictive modeling. By leveraging energy demand, usage, and price models, Market empowers users to make informed decisions about their energy consumption and investment in solar technologies.

![Market](https://raw.githubusercontent.com/hramzan01/project_market/master/app/assets/market_what.png)

### Key Features:
- **Solar Energy Management**: Market specializes in solar energy management, utilizing energy demand, usage, and price models to predict optimum cost savings.

- **Machine Learning and Deep Neural Network Technology**: Leveraging advanced machine learning and deep neural network technology, Market offers sophisticated analysis and predictions for efficient solar energy management.


## Project Directory
```bash
|   .env.yaml
|   .envrc
|   .gitattributes
|   .gitignore
|   .python-version
|   api_test.ipynb
|   Dockerfile
|   Makefile
|   README.md
|   requirements.txt
|   requirements_prod.txt
|   setup.py
|   test.py
|
+---.devcontainer
|       devcontainer.json
|
+---app
|   |   home.py
|   |   predict_cached.json
|   |
|   +---assets
|   |       battery.png
|   |       Bungalow.png
|   |       Detached House.png
|   |       Double solar.png
|   |       Electric vehicle.png
|   |       energy.png
|   |       Flat.png
|   |       Large battery.png
|   |       logo.png
|   |       market_how.png
|   |       market_models.png
|   |       market_optimiser.png
|   |       market_what.png
|   |       money.png
|   |       orange_drop.png
|   |       promo.mp4
|   |       Quad solar.png
|   |       Single solar.png
|   |       Small battery.png
|   |       Terrace house.png
|   |       Triple solar.png
|   |
|   \---config
|           market_ux.drawio
|           timeline.py
|
+---config
|       timeline.py
|
+---energt_price_pred.egg-info
|       dependency_links.txt
|       PKG-INFO
|       requires.txt
|       SOURCES.txt
|       top_level.txt
|
+---energy-price-pred
|       energy-price-pred.py
|       __init__.py
|
+---energypricepred
|       energy-price-pred.py
|       __init__.py
|
+---energypricepred.egg-info
|       dependency_links.txt
|       PKG-INFO
|       requires.txt
|       SOURCES.txt
|       top_level.txt
|
+---energy_price_pred
|   |   energypricepred.py
|   |   energy_price_pred.py
|   |   params.py
|   |   __init__.py
|   |
|   +---api
|   |   |   fast_price.py
|   |   |
|   |   \---__pycache__
|   |           fast_price.cpython-311.pyc
|   |
|   \---__pycache__
|           energypricepred.cpython-311.pyc
|           __init__.cpython-311.pyc
|
+---energy_price_pred.egg-info
|       dependency_links.txt
|       PKG-INFO
|       requires.txt
|       SOURCES.txt
|       top_level.txt
|
+---market
|   |   supply_data.py
|   |   __init__.py
|   |
|   +---api
|   |       fast_price.py
|   |       fast_price_copy.py
|   |
|   +---ml_logic
|   |       cons_model.py
|   |       cons_preprocessor.py
|   |       energy_price_model.py
|   |       gen_model.py
|   |       gen_model_deep.py
|   |       gen_model_efficient.py
|   |       gen_model_updated.py
|   |       optimiser_deep_timecheck.py
|   |       optimiser_model.py
|   |       optimiser_model_evaluation.py
|   |       optimiser_model_eval_deep.py
|   |       optimiser_model_variable_inputs.py
|   |       optimiser_model_variable_inputs_copy_ri.py
|   |       optimiser_model_variable_inputs_copy_ri2.py
|   |       optimsier_model_var_in_deep.py
|   |       optimsier_model_var_in_deep_2.py
|   |       opt_model_deep_eval_v2.py
|   |       opt_model_tester.py
|   |       __init__.py
|   |
|   \---models
|           consumption_model.json
|           deep_model.keras
|           ldn_energy_supply.csv_Zone.Identifier
|           price_model.json
|           rnn_model.keras
|           X_scaler.save
|           Y_scaler.save
|
+---notebooks
|   |   .cache.sqlite
|   |   bmrs_api.ipynb
|   |   eda_dataset.ipynb
|   |   energy-price-anydate.ipynb
|   |   energy-price-anydate_copy.ipynb
|   |   energy-price-past6months.ipynb
|   |   energy-price-pre-mid2020.ipynb
|   |   energy-price.ipynb
|   |   energy_cons_full.ipynb
|   |   energy_cons_full_FO.ipynb
|   |   energy_cons_preliminary.ipynb
|   |   energy_cons_prophet.ipynb
|   |   gen_RNN.ipynb
|   |   HouseholdconsumptionFO.ipynb
|   |   knn model for acorn.ipynb
|   |   optimsation_problem.ipynb
|   |   opt_model.ipynb
|   |   opt_model_variable_inputs.ipynb
|   |   package_test.ipynb
|   |   plot.ipynb
|   |   project_brief.ipynb
|   |   supply_data.ipynb
|   |   supply_refactored.ipynb
|   |   time_series_models copy.ipynb
|   |   time_series_models.ipynb
|   |   weather_data.ipynb
|   |
|   +---data
|   |       csv_agileoutgoing_C_London.csv
|   |       csv_agile_C_London.csv
|   |       csv_tracker_C_London.csv
|   |       stats_models.ipynb
|   |
|   \---simple_lstm
|           checkpoint.weights.h5
|
+---old_py
|       energy-price-pred_old.py
|       energy-price-pred_old2.py
|       energy-price-pred_old3.py
|
\---tests
        __init__.py
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


