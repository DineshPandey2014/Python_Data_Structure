import datetime
import calendar
from datetime import datetime


def monthly_charge(month, subscription, users):
    """ Computes the monthly charge for a given subscription.

    @rtype: int
    @returns: the total monthly bill for the customer in cents, rounded
      to the nearest cent. For example, a bill of $20.00 should return 2000.
      If there are no active users or the subscription is None, returns 0.

    @type month: str
    @param month - Always present
      Has the following structure:
      "2022-04"  # April 2022 in YYYY-MM format

    @type subscription: dict
    @param subscription - May be None
      If present, has the following structure:
      {
        'id': 763,
        'customer_id': 328,
        'monthly_price_in_cents': 359  # price per active user per month
      }

    @type users: list
    @param users - May be empty, but not None
      Has the following structure:
      [
        {
          'id': 1,
          'name': "Employee #1",
          'customer_id': 1,

          # when this user started
          'activated_on': datetime.date(2021, 11, 4),

          # last day to bill for user
          # should bill up to and including this date
          # since user had some access on this date
          'deactivated_on': datetime.date(2022, 4, 10)
        },
        {
          'id': 2,
          'name': "Employee #2",
          'customer_id': 1,

          # when this user started
          'activated_on': datetime.date(2021, 12, 4),

          # hasn't been deactivated yet
          'deactivated_on': None
        },
      ]
    """
    # When either one is None. Return monthly charge as 0
    if subscription == None or users == None:
        return 0

    # Subscription price
    monthly_price_in_cents = subscription["monthly_price_in_cents"]

    billing_month_date = datetime.strptime(month, "%Y-%m").date()
    first_day_for_billing = first_day_of_month(billing_month_date)
    last_day_for_billing = last_day_of_month(billing_month_date)

    # Let's say total bill is 0
    total_bill = 0

    # Iterate each user which is list. And each user in the list is in the form of dict

    for user in users:
        # Now we need to calculate the activation date for each user
        # In case There is no activation date will take first of the month
        # Will take the max date for activation. User can be activated on the any day of the month
        activation_date = max(user['activated_on'], first_day_for_billing)

        # For decativation date let's say there is no decativation date for the month
        # in the case it's continue the subscription for billing will take the last day
        # of the month
        if user['deactivated_on'] == None:
            deactivation_date = last_day_for_billing
        else:
            deactivation_date = user['deactivated_on']

        no_of_days_active_subscription = (deactivation_date - activation_date) + 1

        monthly_subscription_charges_per_user = no_of_days_active_subscription * monthly_price_in_cents

        total_bill = total_bill + monthly_subscription_charges_per_user
        # Return total bill for each user
        return total_bill


####################
# Helper functions #
####################

def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 1)                           # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    >>> last_day_of_month(datetime.date(2022, 3, 17))  # Mar 17
    datetime.date(2022, 3, 31)                         # Mar 31

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    >>> next_day(datetime.date(2022, 3, 17))   # Mar 17
    datetime.date(2022, 3, 18)                 # Mar 18

    >>> next_day(datetime.date(2022, 3, 31))  # Mar 31
    datetime.date(2022, 4, 1)                 # Apr  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)

if __name__ == "__main__":
    # Example usage:
    month = "2022-04"
    subscription = {
        'id': 763,
        'customer_id': 328,
        'monthly_price_in_cents': 359
    }
    users = [
        {
            'id': 1,
            'name': "Employee #1",
            'customer_id': 1,
            'activated_on': datetime.date(2021, 11, 4),
            'deactivated_on': datetime.date(2022, 4, 10)
        },
        {
            'id': 2,
            'name': "Employee #2",
            'customer_id': 1,
            'activated_on': datetime.date(2021, 12, 4),
            'deactivated_on': None
        },
    ]

    total_monthly_bill = monthly_charge(month, subscription, users)
    print(f'Total Monthly Bill: {total_monthly_bill} cents')