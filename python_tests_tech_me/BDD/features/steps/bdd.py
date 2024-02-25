from behave import given, when, then
import pages


@given('I find and select a product')
def step_impl(context):
    context.page = pages.SearchPage(context.driver)
    context.page.find_and_select_product()


@when('I click on the review link')
def step_impl(context):
    context.page = pages.ProductPage(context.driver)
    context.page.opinion_link_click()


@when('I click on the add review button')
def step_impl(context):
    context.page.add_opinion_click()


@then('I should see fields for name, description, phone, and a send button')
def step_impl(context):
    name_opinion, description_opinion, phone_opinion, sent_button_opinion = context.page.check_fields_opinion()
    assert all(field is not None for field in [name_opinion, description_opinion, phone_opinion, sent_button_opinion])


@when('I click on the product image')
def step_impl(context):
    context.page.click_image_product()


@then('I should see the image panel and a close button')
def step_impl(context):
    x_image_button, image_panel = context.page.check_image_panel()
    assert x_image_button is not None
    assert image_panel is not None
