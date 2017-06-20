def get_tukey_outliers(data):
    tukey_outliers = []
    for feature in data.keys():

        ## First Quartile
        Q1 = np.percentile(data.loc[:, feature], 25)

        ## Third Quartile
        Q3 = np.percentile(data.loc[:, feature], 75)

        ## InterQuartile range
        step = 1.5 * (Q3 - Q1)

        # Display the outliers
        print "Data points considered outliers for the feature '{}':".format(feature)

        feature_outlier = data[~((data[feature] >= Q1 - step) & (data[feature] <= Q3 + step))].index
        print feature_outlier.tolist()

        tukey_outliers = tukey_outliers + feature_outlier.tolist()
    return tukey_outliers
