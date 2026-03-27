import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # VALID VALUES
    valid_cities = ['chicago', 'new york city', 'washington']
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Choose a city (chicago, new york city, washington): ").lower()
        if city in valid_cities:
            break
        print("Invalid city. Please try again.\n")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Choose a month (all, january, ... , june): ").lower()
        if month in valid_months:
            break
        print("Invalid month. Please try again.\n")


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input("Enter day of week (all, monday, ..., sunday): ").lower()
    while day not in days:
        day = input("Invalid. Enter day again: ").lower()


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
    
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert Start Time to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month, day, hour
    df['month'] = df['Start Time'].dt.month
    df['day_name'] = df['Start Time'].dt.day_name().str.lower()
    df['hour'] = df['Start Time'].dt.hour

    # MONTH FILTER
    if month != 'all':
        df = df[df['month'] == month]


    # DAY FILTER
    if day != 'all':
        df = df[df['day_name'] == day]

    return df

def display_raw_data(df):
    """Ask user if they want to see raw data, show 5 rows at a time."""
    
    view_data = input("Would you like to see the raw data? Enter yes or no: ").lower()
    start = 0

    while view_data == 'yes':
        print(df.iloc[start:start+5])
        start += 5
        view_data = input("Would you like to see 5 more rows? Enter yes or no: ").lower()

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("Most common month:", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("Most common day of week:", df['day_name'].mode()[0])

    # TO DO: display the most common start hour
    print("Most common start hour:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most commonly used start station:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("Most commonly used end station:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'] + " → " + df['End Station']
    print("Most frequent combination of stations:", df['route'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("Mean travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User Types:")
    print(df['User Type'].value_counts(), "\n")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("Gender Counts:")
        print(df['Gender'].value_counts(), "\n")
    else:
        print("Gender data not available for this city.\n")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest birth year:", int(df['Birth Year'].min()))
        print("Most recent birth year:", int(df['Birth Year'].max()))
        print("Most common birth year:", int(df['Birth Year'].mode()[0]))
    else:
        print("Birth year data not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_raw_data(df)        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()