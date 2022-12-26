# SPICED Week08: Predicting the amount of customers and their movement within a supermarket using a 'Monte-Carlo-Markov-Chain' and 'Object Orientated Programming'

## Project Summary

In this project I predicted the number of customers and their movement within the DOODL Supermarket. The supermarket has four aisles (fruit, spices, dairy, drinks) and one checkout. To do the prediction, I calculated a 'Transition Probability Matrix' based on historical data of customer movements within the supermarket using a 'Monte Carlo Markov Chain'.

The customer movements are calculated every minute, graphically animated and stored in the file ./data/customer.csv.

## Demonstration Video

https://user-images.githubusercontent.com/61935581/209478840-efb8b7ef-0592-4395-ac88-26dc0c6492e8.mp4

Graphic representation of the supermarket

![Bildschirmfoto 2022-12-25 um 19 53 35](https://user-images.githubusercontent.com/61935581/209479227-0de17873-4045-46b7-beec-4cd39be95cb7.png)

## Installation

Clone the repository and create a new virtual environment

```bash
python3 -m venv envname # to create the virtual env
source envname/bin/activate # activate it
```

Afterwards install the libraries specified in requirements.txt

```bash
pip install -r requirements.txt
```

## Usage

The project has several components:

- The jupyter notebook '1_EDA.ipynb' merges the historical data and applies extensive 'data preprocessing'.
- '2_Graphics.ipynb' includes a few graphical analyses of the merged and preprocessed data set.
- '3_probability_matrix.ipynb' contains the central 'transition probability matrix' on the basis of which the movement of customers is estimated.
- 'supermarket_class.py' and 'customer_class.py' contains the classes for the supermarket and the customers according to OOP.
- The simulation can be started via 'main.py'. The graphical representation starts automatically. In addition, the customers and their movements are stored in the file './data/customers.csv'.

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
