@router.get("/")
def root():
    return {
        "service": "WABA Backend Demo",
        "status": "running"
    }
