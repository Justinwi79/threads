import matplotlib as plt
from dask.distributed import LocalCluster, Client
import dask.dataframe as dd
import scipy
from scipy import stats
import statistics
import pandas
df = dd.read_csv("Ubereat_US_Merchant.csv")

def AttributeInfo(attribute):
    #get information on attributes
    print("**********************")
    # print(attribute)
    # print('Possible values - ',df[attribute].unique().compute())
    print('value counts - ')
    # print(df[attribute].value_counts().compute())
    print('Max - ',df['Alexandria'].max().compute())
    # print('Min - ',df[attribute].min().compute())
    print('Central Tendency')
    # print('Mean - ',df[attribute].mean().compute())
    #print('Median - ',df[attribute].median().compute())
    # print('Geometric mean - ',scipy.stats.gmean(df[attribute].compute()))
    print('Variance Metric')
    # print('Standard Deviation - ',statistics.stdev(df[attribute].compute()))


if __name__ == '__main__':
    # client = Client(cluster)
    #To see where the port of the dashboard is, use this command
    # print(client.scheduler_info()['services'])

    ##df = dd.read_json("yelp_academic_dataset_review.json", lines=True, encoding='utf-8', blocksize="100MB")
    # df = dd.read_json("yelp_academic_dataset_review.json", lines=True, encoding='utf-8', blocksize="50MB")
    ##df = dd.read_json("yelp_academic_dataset_review.json", lines=True, encoding='utf-8', blocksize="10MB")

    #show columns
    print("columns=",df.columns)
    print("number of columns",df.shape[1])

    ##print("number of rows",df.shape[0])
    print("number of rows",df.shape[0].compute())

    #get information on all columns
    #print("Information on all columns")
    #print(df.info())

    #AttributeInfo('stars')

    #M RatPerBus
    print('Ratings per Business')

    #print('Mean')
    # print(df.groupby('loc_name').review_count.mean().compute())

    #print('Max')
    #print(df.groupby('loc_name').review_count.max().compute())

    #print('Min')
    print(df.groupby('loc_name').review_count.min().compute())

    # print('value counts - ')
    # print(df.groupby('business_id').stars.value_counts().compute())
