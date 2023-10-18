# Sprint_6

## Project Overview

In this project, we will write automated tests for two main scenarios on the "Yandex.Samokat" website:

1. **Dropdown List Verification** in the "Important Questions" section:
   - Verify that when you click on the dropdown arrow, the corresponding text opens.
   - Write separate tests for each dropdown question.

2. **Scooter Booking Flow**:
   - Check the entire positive flow scenario with two sets of data.
   - Verify two entry points to the scenario: the "Order" button at the top of the page and at the bottom.

### Positive Scenario Steps:

1. Click the "Order" button.
2. The page displays two booking buttons.
3. Fill out the order form.
4. Verify that a popup message confirming the successful creation of the order appears.
5. Check that clicking the "Samokat" logo leads to the "Samokat" homepage.
6. Check that clicking the Yandex logo opens the Yandex Zen homepage in a new window through redirection.

We need to create tests for multiple data sets, with at least two sets of data. The scenario remains the same for both entry points; there is no need to retest each of them.

## Project Structure

### Prerequisites

- Install the Mozilla Firefox browser.
- Install and set up Selenium and Allure.

### Project Directory Structure

- **pages**: Contains page objects with locators and actions.
- **tests**: Contains test scripts. Each test class can group tests based on functionality or theme.
- **allure_results**: This directory stores Allure report data.
- **conftest.py**: Configuration file for pytest fixtures and settings.
- **README.md**: This file provides an overview of the project, its structure, and instructions for running tests and generating Allure reports.

### Running Tests

pytest tests --alluredir=allure_results

