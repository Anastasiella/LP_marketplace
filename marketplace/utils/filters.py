from .. import app


@app.template_filter('format_data_to_hr')
def format_data_to_hr(date_of_item):
    return date_of_item.strftime("%Y-%m-%d %H:%M:%S")
