# declaring stack

browsing_session = []
# adding value
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

# stack follows lifo approach

browsing_session.pop()

print(browsing_session)

last = browsing_session[-1]
print(last)

# before cheking last value , must check weather stack is empty or NotImplemented

if not browsing_session:
    browsing_session[-1]
