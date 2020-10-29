from .. import app


@app.template_filter('format_data_to_human_readable')
def format_data_to_human_readable(date_of_item):
    return date_of_item.strftime("%Y-%m-%d %H:%M:%S")
