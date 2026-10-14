# Snapfood Sentiment Analysis

A machine-learning project that classifies Persian Snapfood comments into two sentiment categories: **HAPPY** and **SAD**. It uses TF-IDF to convert text into numerical features and a `LinearSVC` classifier to predict sentiment. A simple Tkinter interface lets the user enter a comment and view an image corresponding to the prediction.

## Features

- Loads labeled training and test data from CSV files.
- Converts comments into TF-IDF features using unigrams, bigrams, and trigrams.
- Trains a `LinearSVC` sentiment classifier.
- Predicts labels for the test dataset and saves the predictions to an Excel file.
- Prints a classification report with precision, recall, F1-score, and support.
- Provides a graphical interface for testing a single comment.
- Displays `1.ico` for **HAPPY** predictions and `3.ico` for **SAD** predictions.

## Technologies

- Python
- pandas
- scikit-learn
- Tkinter
- Pillow
- openpyxl (for writing the Excel output)

## Project Files

Make sure these files are in the same folder as the Python script:

```text
project/
├── main.py
├── snapfood_train(1).csv
├── snapfood_test(1).csv
├── 1.ico
├── 3.ico
└── test.xlsx              # generated when the script runs
```

The CSV files must contain the columns `comment` and `label`. The labels in the `label` column should match the classes used by the model, such as `HAPPY` and `SAD`.

## Installation

Install the required packages:

```bash
pip install pandas scikit-learn pillow openpyxl
```

Tkinter is usually included with standard Python installations. On some Linux distributions, it may need to be installed separately.

## How to Run

1. Place the training CSV, test CSV, and image files in the project folder.
2. Install the dependencies.
3. Run the Python script:

   ```bash
   python main.py
   ```

4. The script trains the model, predicts sentiment for the test comments, saves the results to `test.xlsx`, and prints the classification report in the terminal.
5. A window opens. Enter a comment in the input field and click **Enter** to display the predicted sentiment image.

## Model Details

### Text preprocessing

The `TfidfVectorizer` uses:

- `ngram_range=(1, 3)`: extracts one-word, two-word, and three-word features.
- `min_df=1`: keeps terms that occur in at least one document.
- `max_df=0.98`: ignores terms that appear in more than 98% of documents.

### Classifier

The project uses `LinearSVC`, a linear support vector classifier that works well with sparse, high-dimensional text features.

### Evaluation

The model predicts labels for the test comments. The script compares predictions with the true `label` values and prints a classification report containing:

- **Precision:** how many predictions for a class were correct.
- **Recall:** how many actual examples of a class were found.
- **F1-score:** the harmonic mean of precision and recall.
- **Support:** the number of true examples in each class.

The report values depend on the CSV files and the trained model, so they are not specified in advance.

## Software Output

The following image shows the software output and model results:

![Model Output](a.png)

## Output

- `test.xlsx`: test dataset with an additional `prediction` column.
- Terminal classification report.
- Tkinter window for entering and classifying a single comment.

## Notes and Troubleshooting

- If a CSV file cannot be found, check that its filename and location exactly match the names in the script.
- If `comment` or `label` causes a `KeyError`, verify the CSV column names.
- If an image does not appear, check that `1.ico` and `3.ico` exist in the project folder and are valid image files that Pillow can open. Despite the `.ico` extension, the files are loaded through Pillow.
- If the test dataset contains fewer than 9,033 rows, the loop `range(9033)` will cause an indexing error. A safer version is:

  ```python
  for comment in d_test["comment"]:
      p = model.predict(tf.transform([comment]))
      o.append(p[0])
  ```

- If the model is trained and evaluated on the same or overlapping data, the reported performance may not reflect how well it generalizes to unseen comments.

## Possible Improvements

- Add a visible text result (`HAPPY` or `SAD`) alongside the image.
- Clear or replace the previous image each time a new prediction is made.
- Handle empty input and missing comments.
- Use `len(d_test)` instead of a fixed row count when generating predictions.
- Save the trained model and vectorizer so they do not need to be retrained every time the program starts.


