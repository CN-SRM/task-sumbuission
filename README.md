# Breast Cancer Detection using K-Means Clustering

This project implements a clustering model for breast cancer detection using the Breast Cancer Wisconsin (Diagnostic) Data Set. The main focus is on exploring the K-Means clustering algorithm to group similar instances together. The dataset contains features computed from a digitized image of a fine needle aspirate (FNA) of a breast mass.

## Table of Contents
- [Introduction](#introduction)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Results](#results)
- [Dependencies](#dependencies)

## Introduction

Breast cancer is a significant health concern, and early detection is crucial for successful treatment. This project aims to apply K-Means clustering to identify patterns and groupings in breast cancer data, potentially aiding in the detection of malignant and benign cases.

## Dataset

The dataset used in this project is the Breast Cancer Wisconsin (Diagnostic) Data Set, which can be found on Kaggle: [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data).

## Project Structure

The project is structured as follows:

- **data.csv**: CSV file containing the Breast Cancer Wisconsin dataset.
- **Clustering_Cancer_Detection.ipynb**: Jupyter Notebook containing the code for the clustering model.
- **model1.pkl**: Pickle file storing the trained K-Means clustering model.
- **main.py**: The FastAPI code for using the clustering model in webpages.
- **/templates/**: Directory for the webpage HTML files.
- **/static/**: Directory for the static files like images and css files for the webpages.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/nabhpatodi10/Cancer-Detection-Clustering-Model.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Cancer-Detection-Clustering-Model
   ```

3. Open and run the `Clustering_Cancer_Detection.ipynb` Jupyter Notebook to explore the code and visualize the clustering results.

4. If needed, use the saved K-Means model (`model1.pkl`) for predictions in your application.

5. You can also run the FastAPI for this model using the Python File `main.py` which is connected to the webpages in the `/templates/` directory.

## Results

The project includes visualizations of the data, the Elbow Method for determining the optimal number of clusters (K), and scatter plots illustrating the K-Means clustering results. Additionally, a crosstabulation is provided to compare the clustering results with the original diagnosis labels.

## Dependencies

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

Install the required dependencies using:

```bash
pip install pandas
```
```bash
pip install numpy
```
```bash
pip install matplotlib
```
```bash
pip install seaborn
```
```bash
pip install scikit-learn
```

Feel free to fork and adapt this project for your own use.
