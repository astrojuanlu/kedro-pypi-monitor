# Kedro PyPI monitor

## Installation

```
$ uv pip install -r requirements.txt -r dev-requirements.txt
```

Or, with plain `pip`:

```
$ pip install -r requirements.txt -r dev-requirements.txt
```

## Authentication

<details>
<summary>Generate a JSON credentials file from Google BigQuery. Click to expand steps.</summary>

<!-- Taken from https://github.com/ofek/pypinfo/blob/0720138/README.md -->

### Create project

1. Go to https://bigquery.cloud.google.com.
2. Sign up if you haven't already. The first TB of queried data each month is free. Each additional TB is $5.

3. Sign in on your account if you are not already;

4. Go to https://console.developers.google.com/cloud-resource-manager and click CREATE PROJECT if you don't already have one:

![create](https://user-images.githubusercontent.com/1324225/47172949-6f4ea880-d315-11e8-8587-8b8117efeae9.png "CREATE PROJECT")

5. This takes you to [https://console.developers.google.com/projectcreate](https://console.developers.google.com/projectcreate). Fill out the form and click CREATE. Any name is fine, but I recommend you choose something to do with PyPI like pypinfo. This way you know what the project is designated for:

![click](https://user-images.githubusercontent.com/1324225/47173020-986f3900-d315-11e8-90ab-4b2ecd85b88e.png)

6. A while after creation, at the left-top corner, select the project name of your choice on dropdown component AND at the left-top corner "Navigation Menu", select option "Cloud Overview > Dashboard":

![show](https://user-images.githubusercontent.com/1324225/47173170-0b78af80-d316-11e8-879e-01f34e139b80.png)

### Enable BigQuery API

7. Click on top-left button "Navigation Menu" and click on option "API and services > Library":

![api_library](https://user-images.githubusercontent.com/13961685/224557997-6842161c-6589-4c2a-8974-6bb3c8dc0b0b.png)

8. Perform a search with keywords "big query api" on available text field:

![big_query_api_search](https://user-images.githubusercontent.com/13961685/224558113-4f3a3006-3216-41e9-9554-3ce60da60fd1.png)

9. Enable Big Query API by button "Enable" press:

![big_query_api](https://user-images.githubusercontent.com/13961685/224558381-4af65bf6-348b-4e48-bd14-d667c4a6e1c7.png)

10. After enabling, click CREATE CREDENTIALS:

![credentials](https://user-images.githubusercontent.com/1324225/47173432-bc7f4a00-d316-11e8-8152-6a0e6cfab70f.png)

**Note**: You will be requested to go back to Big Query panel. In this case, click on top-left button "Navigation Menu", option "API and services > Enabled APIs and services" and on consequent page, on item "Big Query API":

![enabled_credentials](https://user-images.githubusercontent.com/13961685/224572489-402be9b3-a441-45f0-a469-df3a292b2d80.png)

11. On the page after clicking the "CREATE CREDENTIALS" button, choose "BigQuery API", "Application Data" and "No, I'm not using them":

![credentials_page_1](https://user-images.githubusercontent.com/13961685/224556508-e57d9ea0-564c-45db-b553-a53f60c307af.png)

12. Fill account details and press button "Create and Continue":

![credentials_page_2](https://user-images.githubusercontent.com/13961685/224557099-e0e4785d-5af8-41d8-b179-5df7c49fca79.png)

13. Select role "BigQuery User" (option path "BigQuery > Big Query User"), press button "Done":

![credentials_page_3](https://user-images.githubusercontent.com/13961685/224557170-73532a10-ad64-4e74-9018-8c5f8ad205d7.png)

14. On Big Query API panel (See **Note** on item *10*), click on tab "CREDENTIALS". On section "Service accounts", click on created credentials on items 11, 12 and 13.

![create_service_credential_key](https://user-images.githubusercontent.com/13961685/224572983-d005fef7-9490-429a-bd6b-58616dd6cc86.png)

15. On page from credential click, click on tab "KEYS". On dropdown menu "ADD KEY", click on option "Create new key":

![create_credential_key](https://user-images.githubusercontent.com/13961685/224573182-5d812f47-c1c5-4aaa-a774-6ae00ce8250d.png)

16. On appearing box, click on option "JSON" and press button "CREATE": This will start the download of credentials on a JSON file with name pattern `{name}-{credentials_hash}.json`:

![create_private_key](https://user-images.githubusercontent.com/13961685/224573235-70f35826-73bb-4dad-bcbf-e6267d105121.png)

</details>

Then, export the `GOOGLE_APPLICATION_CREDENTIALS` environment variable with the path to that file:

```bash
$ export GOOGLE_APPLICATION_CREDENTIALS=kedro-pypi-stats-xxx.json
```

## Test

To test that the code works, run the demo pipeline:

```bash
$ KEDRO_ENV=demo kedro run --pipeline fetch_kedro_data
[08/02/24 08:43:25] INFO     Kedro project kedro-pypi-monitor                  session.py:324
[08/02/24 08:43:29] INFO     Using synchronous mode for loading and   sequential_runner.py:64
                             saving data. Use the --async flag for
                             potential performance gains.
                             https://docs.kedro.org/en/stable/nodes_a
                             nd_pipelines/run_a_pipeline.html#load-an
                             d-save-asynchronously
                    INFO     Loading data from pypi_kedro_raw             data_catalog.py:508
                             (PolarsBigQueryDataset)...
[08/02/24 08:43:33] INFO     Running node: unnest_data([pypi_kedro_raw]) ->       node.py:361
                             [pypi_kedro_unnested]
                    INFO     Saving data to pypi_kedro_unnested           data_catalog.py:550
                             (EagerPolarsDataset)...
                    INFO     Completed 1 out of 1 tasks               sequential_runner.py:90
                    INFO     Pipeline execution completed successfully.         runner.py:119
```
