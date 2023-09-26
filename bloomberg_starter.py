import blpapi

sessionOptions = blpapi.SessionOptions()
sessionOptions.setServerHost("localhost")  # Bloomberg server host
sessionOptions.setServerPort(8194)         # Bloomberg server port

session = blpapi.Session(sessionOptions)
session.start()

if session.openService("//blp/refdata"):
    service = session.getService("//blp/refdata")
    request = service.createRequest("ReferenceDataRequest")
    request.getElement("securities").appendValue("AAPL US Equity")
    request.getElement("fields").appendValue("PX_LAST")

    session.sendRequest(request)

    while True:
        event = session.nextEvent()
        if event.eventType() == blpapi.Event.RESPONSE:
            for msg in event:
                print(msg)
                # Process the response message here

    session.stop()
