from setuptools import setup

setup(name = 'kmeans-feature-importance',
      version = '1.0',
      description = 'kmeans_interp is a wrapper around sklearn.cluster.KMeans which adds the property feature_importances_ that will act as a cluster-based feature weighting technique. Features are weighted using either of the two methods: wcss_min or unsup2sup.',
      author = 'Yousef Alghofaili',
      url = 'https://github.com/YousefGh/kmeans-feature-importance',
      package_dir = {'kmeans_interp': 'kmeans_interp'},
      install_requires = ['scikit-learn>=0.24.2',
                          'numpy'])
