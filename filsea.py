import os
from datetime import datetime

def search_files(keyword, file_type=None, min_size=None, max_size=None, start_date=None, end_date=None):
    matches = []
    for root, dirnames, filenames in os.walk('/'):
        for filename in filenames:
            if keyword in filename:
                file_path = os.path.join(root, filename)
                if file_type and not filename.endswith(file_type):
                    continue
                if min_size or max_size:
                    size = os.path.getsize(file_path)
                    if min_size and size < min_size:
                        continue
                    if max_size and size > max_size:
                        continue
                if start_date or end_date:
                    mtime = os.path.getmtime(file_path)
                    date_modified = datetime.fromtimestamp(mtime)
                    if start_date and date_modified < start_date:
                        continue
                    if end_date and date_modified > end_date:
                        continue
                matches.append(file_path)
    return matches

if __name__ == '__main__':
    print('Welcome to Filsea - Fast File Search')
    keyword = input('Enter the file name to search for: ')
    file_type = input('Enter the file type to filter by (e.g. .txt, .pdf) or leave blank: ')
    min_size = input('Enter the minimum file size in bytes or leave blank: ')
    max_size = input('Enter the maximum file size in bytes or leave blank: ')
    start_date_str = input('Enter the start date for date modified (YYYY-MM-DD) or leave blank: ')
    end_date_str = input('Enter the end date for date modified (YYYY-MM-DD) or leave blank: ')

    min_size = int(min_size) if min_size else None
    max_size = int(max_size) if max_size else None
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d') if start_date_str else None
    end_date = datetime.strptime(end_date_str, '%Y-%m-%d') if end_date_str else None

    results = search_files(keyword, file_type=file_type, min_size=min_size, max_size=max_size, start_date=start_date, end_date=end_date)
    print(f'Found {len(results)} results:')
    for result in results:
        print(result);