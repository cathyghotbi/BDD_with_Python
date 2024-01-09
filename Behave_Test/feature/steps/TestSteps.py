from behave import *

from addition import addition


@given(u'input')
def step_given_input(context):
    context.a = 1
    context.b = 2


@when(u'add')
def step_when_added_input(context):
    context.res = addition(context.a, context.b)


@then(u'result')
def step_then_3(context):
    assert context.res == 3


# annotaions (@given, @when, @then) map these step func to the corresponding steps in feature files
@given(u'two numbers, {first_number:d} and {second_number:d}')
def step_given_numbers(context, first_number, second_number):
    if first_number < 0:
        raise Exception("'{first_number}' is not valid because it is negative")
    if second_number < 0:
        raise Exception("'{second_number}' is not valid because it is negative")
    context.x = first_number
    context.y = second_number


@when(u'two numbers')
def step_when_added(context):
    context.sum = addition(int(context.x), int(context.y))


@then(u'{result:d}')
def step_then_result(context, result):
    assert context.sum == result
