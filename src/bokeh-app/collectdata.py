#!/usr/bin/env python3

import pdb
import os
import wget
import shutil
import pandas


def download_file(f):
    fname = os.path.basename(f)
    if os.path.exists(fname):
        os.remove(fname)
    wget.download(f)

def collect(outpath='.'):
    # download the latest NYTs data
    baseUrl = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'    
    
    # Read in the frame, set the index as dates, and parse the dates
    df = pandas.read_csv(baseUrl, parse_dates=['date'], index_col='date', header=0)
        
    # Columns to subset
    cs, ds = ['state', 'cases'], ['state', 'deaths']
    confirmed, deaths = df[cs], df[ds]                                  
        
    for data, fname in zip([confirmed, deaths], ['time_series_covid19_confirmed_US.csv', 'time_series_covid19_deaths_US.csv']):
        # clean state names, i.e. remove spaces
        data.loc[:,'state'] = data.state.str.replace(' ', '_')
            
        # index by unique date with columns of 'states' and i,j values of cases or deaths
        clean_data = pandas.pivot_table(data=data, index=data.index, columns=data['state']).fillna(0).astype(int)
        
        # Select only the states as columns as opposed to ('cases', 'Alabama'), etc
        clean_data.columns = clean_data.columns.get_level_values(1)
        
        # save to csv
        clean_data.to_csv(f'{outpath}/covid-{fname.split("_")[-2]}.tsv', 
                          sep='\t',
                          date_format='%Y%m%d')

        # remove the raw data
        #os.remove(fname)

def old_collect(outpath='.'):
    # download the latest data
    baseUrl = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series'
    deaths = 'time_series_covid19_deaths_US.csv'
    confirmed = 'time_series_covid19_confirmed_US.csv'

    for fname in [deaths, confirmed]:
        print(f'processing {fname}')

        # get file
        download_file(f'{baseUrl}/{fname}')

        # load data
        df = pandas.read_csv(fname)

        # ignore extra columns
        reg_filter = 'Province_State|[0-9]?[0-9]\\/[0-9]?[0-9]\\/[0-9][0-9]'
        df = df.filter(regex=(reg_filter))

        # group data by state
        df = df.groupby('Province_State').sum()

        # clean state names, i.e. remove spaces
        df.index.str.replace(' ', '_')

        # transpose the data
        df = df.T

        # name the index
        df.index.rename('date', inplace=True)
        df.index = pandas.to_datetime(df.index)

        # save to csv
        df.to_csv(f'{outpath}/covid-{fname.split("_")[-2]}.tsv', sep='\t',
                  date_format='%Y%m%d')

        # remove the raw data
        os.remove(fname)


if __name__ == '__main__':
    collect()
