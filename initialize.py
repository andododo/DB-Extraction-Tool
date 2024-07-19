import table_list
import extract

selected_table = table_list.fetch()
extract.all(selected_table)