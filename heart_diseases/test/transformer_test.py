import unittest
import src

INPUT_DATA_PATH = 'test/csv/test_train.csv'
FEATURE_PARAMS = src.FeatureParams(deleted_features=['fbs'],
                                   target_column='condition',
                                   normalize_features=['age', 'trestbps', 'chol', 'thalach', 'oldpeak'])


class TransformerTest(unittest.TestCase):
    def test_simple(self):
        dataset = src.read_csv_data(INPUT_DATA_PATH)
        transformer = src.features.build_transformer(FEATURE_PARAMS)
        transformer.fit(dataset)
        dataset_transformed = transformer.fit_transform(dataset)
        self.assertEqual(dataset.to_numpy().shape, dataset_transformed.shape)