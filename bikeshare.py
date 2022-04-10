import time
import pandas as pd
import numpy as np

#viewed file 4/8
#Udacity project
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

cities = ['chicago', 'new york city', 'washington']
months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = str(input('Enter city (Chicago, New York City or Washington) to analyze data\n').lower())
            if city in cities:
                break
        except (ValueError, KeyboardInterrupt):
            print('Please try again\n')
        else:
            print('Choose (Chicago, New York City or Washington)\n')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = str(input('Enter month (January, February, March, April, May, June or type \"all\") to analyze data\n').lower())
            if month in months:
                break
        except (ValueError, KeyboardInterrupt):
            print('Please try again\n')
            break
        else:
            print('Choose (January, February, Mar, April, May, June or type \"all\")\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = str(input('Enter day Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or type \"all\") to analyze data\n').lower())
            if day in days:
                break
        except (ValueError, KeyboardInterrupt):
            print('Please try again\n')
            break
        else:
            print('Choose day\n')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
	# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['All','January', 'February', 'March', 'April', 'May', 'June']
    common_month = df['month'].mode()[0]
    print ('\nMost common month is: ',months[common_month])

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print ('\nMost common day is: ',common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print ('\nMost common hour is: ',common_hour)

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print('\nThe most commonly used end station is: ',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['combo'] = df['Start Station'] + ' to ' + df['End Station']
    frequent_combination = df['combo'].mode()[0]
    print('\nMost frequent start station is: ',frequent_combination)

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time: ', travel_time)

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('\nMean travel time: ', mean_time)

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()   
    print('User Types:\n',user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('Gender:\n',gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early_year = df['Birth Year'].min()
        print('\nEarliest Year: ',int(early_year))
        recent_year = df['Birth Year'].max()
        print('\nMost Recent Year: ',int(recent_year))
        common_year = df['Birth Year'].mode()[0]
        print('\nMost Common Year: ',int(common_year))

    print("\nThis took %s seconds." % round(time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input('\nWould you like to see 5 lines of raw data? \nEnter yes or no.\n')
        if raw_data.lower() == 'yes':
            r= 0
            while True:
                print(df.iloc[r:r+5])
                r += 5
                five_more = input('\nWould you like to see 5 more lines of data? Enter yes or no: ').lower()
                if five_more != 'yes':
                    break           
            break 
        else: break


if __name__ == "__main__":
	main()