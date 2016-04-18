def safe(func, *args, **kargs):
    try:
        func(*args, **kargs)
    except Exception:
        import sys
        import traceback
        print(sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2],)
        print('\nCatched the error...\n') 
        traceback.print_exc()
        print('\n...and told you where it happened.\n') 
    else:
        print('Function returned without any Exceptions.')
