import pandas as pd

# It appears that 'condition1' and 'condition2' are no longer present.
# Re-loading the file to reset the data for processing correctly
file_path = 'ady.csv'
data = pd.read_csv(file_path)

# Apply the categorization function to reset the conditions
def categorize_condition(condition):
    new_conditions = {
        'a_new': ['chính hãng đã kích hoạt', 'chưa active - đỏ', 'đã kích hoạt', 
                'đã kích hoạt bảo hành', 'đã kích hoạt bảo hành vn/a', 
                'đã kích hoạt online', 'đen - đã kích hoạt', 'đổi bảo hành', 
                'hàng trưng bày', 'mới 100% tbh', 'mới fullbox', 
                'online - đã kích hoạt', 'xanh dương - đã kích hoạt', 
                'không trầy xước'],
        'a_old': ['cũ', 'cũ - trầy xước', 'cũ | chính hãng việt nam', 'cũ 98%', 
                'cũ đẹp lỗi face id', 'cũ trầy xước-đen', 'cũ trầy xước-xanh đen', 
                'cũ xước cấn', 'đổi bảo hành vn/a', 'trầy xước', 
                'trầy xước nhiều', 'cũ trầy xước'],
        'a_like_new': ['cũ - đẹp', 'cũ 99%', 'cũ chính hãng 99%', 'cũ đẹp', 
                     'cũ đẹp 128gb 99%', 'cũ đẹp 99%', 'cũ đẹp-đen', 
                     'cũ đẹp-xám', 'trầy xước ít']
    }
    
    # Lowercase the condition for case-insensitive matching
    condition = condition.lower().strip()
    
    # Check which category the condition belongs to
    for category, conditions in new_conditions.items():
        if condition in conditions:
            return category
    return condition  # Return the original condition if no match is found

# Apply the categorization function to both condition1 and condition2 columns
data['condition1'] = data['condition1'].fillna('').apply(categorize_condition)
data['condition2'] = data['condition2'].fillna('').apply(categorize_condition)

# Replace values in 'condition1' and 'condition2' that are not in ['new', 'old', 'like_new'] with empty strings
valid_conditions = ['a_new', 'a_old', 'a_like_new']
data['condition1'] = data['condition1'].apply(lambda x: x if x in valid_conditions else '')
data['condition2'] = data['condition2'].apply(lambda x: x if x in valid_conditions else '')

# Combine condition1 and condition2 into a single column named 'combined_condition'
data['combined_condition'] = data['condition1'] + ' ' + data['condition2']

# Drop the old columns condition1 and condition2
data = data.drop(columns=['condition1', 'condition2'])

# Save the modified data to a new CSV file
cleaned_combined_file_path = 'handledcondition.csv'
data.to_csv(cleaned_combined_file_path, index=False)

cleaned_combined_file_path
