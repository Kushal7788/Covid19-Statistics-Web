import pandas as pd
from django.shortcuts import render


# Create your views here.

def index(request):
    global_df = pd.read_csv(
        'media/ML Datasets/global_covid19/time_series_covid19_confirmed_global.csv')
    india_df = global_df[global_df['Country/Region'] == 'India']
    india_df = pd.DataFrame.transpose(india_df)
    india_df = india_df.iloc[4:, :]
    india_df.rename(columns={131: 'cases'}, inplace=True)
    india_df.reset_index(level=0, inplace=True)
    india_df.rename(columns={'index': 'date'}, inplace=True)
    india_df['date'] = pd.to_datetime(india_df['date'])
    india_df['date'] = india_df['date'].dt.date
    dates = india_df['date'].tolist()
    over_cases = india_df['cases'].values.tolist()

    state_df = pd.read_csv(
        'media/ML Datasets/covid19_corona_india/state_level_latest.csv')
    state_df = state_df.iloc[1:, :]
    states = state_df['State'].values.tolist()
    st_cases = state_df['Confirmed'].values.tolist()

    dist_df = pd.read_csv(
        'media/ML Datasets/covid19_corona_india/district_level_latest.csv')
    dist_df = dist_df[dist_df['State'] == 'Maharashtra']
    dist = dist_df.District.values.tolist()
    dt_cases = dist_df.Confirmed.values.tolist()

    pune_df = pd.read_csv('media/ML Datasets/Pune/pmc_1.csv')
    pune_df['Date'] = pd.to_datetime(pune_df['Date'])
    pune_df['Date'] = pune_df['Date'].dt.date
    p_dates = pune_df['Date'].tolist()
    p_cases = pune_df['totalconfirmed'].values.tolist()

    # dates = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    # values = [0, 10, 5, 2, 20, 30, 45]
    return render(request, 'index/dash.html', {'dates': dates, 'over_cases': over_cases,
                                               'states': states, 'st_cases': st_cases,
                                               'dists': dist, 'dt_cases': dt_cases,
                                               'p_dates': p_dates, 'p_cases': p_cases})


def death_stat(request):
    global_df = pd.read_csv(
        'media/ML Datasets/global_covid19/time_series_covid19_deaths_global.csv')
    india_df = global_df[global_df['Country/Region'] == 'India']
    india_df = pd.DataFrame.transpose(india_df)
    india_df = india_df.iloc[4:, :]
    india_df.rename(columns={131: 'deaths'}, inplace=True)
    india_df.reset_index(level=0, inplace=True)
    india_df.rename(columns={'index': 'date'}, inplace=True)
    india_df['date'] = pd.to_datetime(india_df['date'])
    india_df['date'] = india_df['date'].dt.date
    dates = india_df['date'].tolist()
    over_cases = india_df['deaths'].values.tolist()

    state_df = pd.read_csv(
        'media/ML Datasets/covid19_corona_india/state_level_latest.csv')
    state_df = state_df.iloc[1:, :]
    states = state_df['State'].values.tolist()
    st_cases = state_df['Deaths'].values.tolist()

    dist_df = pd.read_csv(
        'media/ML Datasets/covid19_corona_india/district_level_latest.csv')
    dist_df = dist_df[dist_df['State'] == 'Maharashtra']
    dist = dist_df.District.values.tolist()
    dt_cases = dist_df.Deceased.values.tolist()

    pune_df = pd.read_csv('media/ML Datasets/Pune/pmc_1.csv')
    pune_df['Date'] = pd.to_datetime(pune_df['Date'])
    pune_df['Date'] = pune_df['Date'].dt.date
    p_dates = pune_df['Date'].tolist()
    p_cases = pune_df['totaldeceased'].values.tolist()

    # dates = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    # values = [0, 10, 5, 2, 20, 30, 45]
    return render(request, 'index/death_stats.html', {'dates': dates, 'over_cases': over_cases,
                                                      'states': states, 'st_cases': st_cases,
                                                      'dists': dist, 'dt_cases': dt_cases,
                                                      'p_dates': p_dates, 'p_cases': p_cases})
