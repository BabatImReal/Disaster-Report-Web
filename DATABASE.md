# **Disaster Report Website - MongoDB Database Schema**

## **Overview**
This database stores disaster reports, alerts, user details, and subscriptions for a disaster report website. It is designed to efficiently manage real-time disaster data and notify users based on their subscriptions.

## **Collections**
The database consists of four main collections:
- `persons` (User details)
- `reports` (Disaster reports submitted by users)
- `alerts` (Disaster alerts with severity levels)
- `subscriptions` (User alert subscriptions)

---

## **1. Persons Collection**
Stores user information, including contact details and roles.

### **Example Document:**
```json
{
  "_id": ObjectId("601c8b15fc13ae1b00000000"),
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "phone": "+1234567890",
  "role": "Admin"
}
```

### **Fields:**
- `_id` : Unique user identifier (ObjectId)
- `name` : Full name of the user
- `email` : User's email address
- `phone` : Contact number
- `role` : User role (e.g., Admin, Reporter, Viewer)

---

## **2. Reports Collection**
Stores disaster reports submitted by users, including location details.

### **Example Document:**
```json
{
  "_id": ObjectId("601c8b15fc13ae1b00000001"),
  "source": {
    "email": "reporter@example.com",
    "phone": "+9876543210"
  },
  "location": {
    "longitude": 106.8456,
    "latitude": -6.2088,
    "country": "Indonesia",
    "city": "Jakarta"
  },
  "timestamp": ISODate("2024-03-28T14:00:00Z")
}
```

### **Fields:**
- `_id` : Unique report identifier (ObjectId)
- `source` : Contains `email` and `phone` of the reporter
- `location` : Stores `longitude`, `latitude`, `country`, and `city`
- `timestamp` : Time when the report was submitted

---

## **3. Alerts Collection**
Stores disaster alerts with severity levels and time range.

### **Example Document:**
```json
{
  "_id": ObjectId("601c8b15fc13ae1b00000002"),
  "type": "Flood",
  "level": "Severe",
  "time": {
    "from": ISODate("2024-03-28T08:00:00Z"),
    "to": ISODate("2024-03-28T18:00:00Z")
  },
  "location": {
    "longitude": 100.5231,
    "latitude": 13.7367,
    "country": "Thailand",
    "city": "Bangkok"
  }
}
```

### **Fields:**
- `_id` : Unique alert identifier (ObjectId)
- `type` : Type of disaster (e.g., Flood, Earthquake, Wildfire)
- `level` : Severity level (e.g., Minor, Moderate, Severe)
- `time` : Contains `from` and `to` timestamps
- `location` : Stores `longitude`, `latitude`, `country`, and `city`

---

## **4. Subscriptions Collection**
Stores user subscriptions for disaster alerts based on location.

### **Example Document:**
```json
{
  "_id": ObjectId("601c8b15fc13ae1b00000003"),
  "user_id": ObjectId("601c8b15fc13ae1b00000000"),
  "location": {
    "country": "Vietnam",
    "city": "Ho Chi Minh City"
  }
}
```

### **Fields:**
- `_id` : Unique subscription identifier (ObjectId)
- `user_id` : References `_id` from `persons` collection
- `location` : Stores `country` and `city`

---
