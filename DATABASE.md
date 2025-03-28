# **Disaster Report Website - MongoDB Database Schema**

## **Overview**
This database stores disaster reports, alerts, user details, and subscriptions for a disaster report website. It is designed to efficiently manage real-time disaster data and notify users based on their subscriptions.

## **Collections**
The database consists of 5 main collections:
- `persons` (User details)
- `reports` (Disaster reports submitted by users)
- `alerts` (Disaster alerts with severity levels)
- `subscriptions` (User alert subscriptions)
- `news` (News articles)

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
    "name": "AnHuyDiet",
    "email": "reporter@example.com",
    "phone": "+9876543210"
  },
  "location": {
    "longitude": 106.8456,
    "latitude": -6.2088,
    "country": "Indonesia",
    "city": "Jakarta"
  },
  "timestamp": ISODate("2024-03-28T14:00:00Z"),
  "description": "Heavy flooding due to continuous rainfall, roads submerged."
}
```

### **Fields:**
- `_id` : Unique report identifier (ObjectId)
- `source` : Contains `name`, `email` and `phone` of the reporter
- `location` : Stores `longitude`, `latitude`, `country`, and `city`
- `timestamp` : Time when the report was submitted
- `description` : more detail about the disaster 

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
  },
  "source": ObjectId("601c8b15fc13ae1b00000001"),
  "admin": ObjectId("601c8b15fc13ae1b00000000")
}
```

### **Fields:**
- `_id` : Unique alert identifier (ObjectId)
- `type` : Type of disaster (e.g., Flood, Earthquake, Wildfire)
- `level` : Severity level (e.g., Minor, Moderate, Severe)
- `time` : Contains `from` and `to` timestamps
- `location` : Stores `longitude`, `latitude`, `country`, and `city`
- `source`: Identifier of the report of the disaster
- `admin` : Identifier of the admin that verifies the alert.

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

# **News Collection**  
Stores news articles related to disasters, including multiple media types such as images and videos.  

## **Example Document**  
```json
{
  "_id": ObjectId("601c8b15fc13ae1b00000004"),
  "title": "Severe Flooding Hits Jakarta",
  "content": "Heavy rainfall has led to severe flooding in Jakarta, affecting thousands of residents...",
  "media": [
    {
      "name": "jakarta-flood-image",
      "url": "https://cdn.example.com/floods/jakarta-1.jpg",
      "type": "image",
      "description": "Flooded streets in Jakarta"
    },
    {
      "name": "jakarta-flood-video",
      "url": "https://cdn.example.com/floods/jakarta-video.mp4",
      "type": "video",
      "thumbnail": "https://cdn.example.com/floods/jakarta-thumbnail.jpg",
      "description": "Drone footage of the flood"
    }
  ],
  "source": {
    "name": "Jakarta Post",
    "url": "https://jakartapost.com/news/flooding-2024"
  },
  "timestamp": ISODate("2024-03-28T10:30:00Z"),
  "disaster_type": "Flood",
  "location": {
    "country": "Indonesia",
    "city": "Jakarta"
  }
}
```

## **Fields**  

- **`_id`** : Unique identifier for the news article (ObjectId).  
- **`title`** : Title of the news article.  
- **`content`** : Full text content of the news article.  
- **`media`** : Array of media files (images, videos, etc.). Each media object includes:  
  - **`name`** : Unique name for the media file.  
  - **`url`** : Direct link to the media file.  
  - **`type`** : Type of media (`image`, `video`, `audio`).  
  - **`description`** *(optional)* : Short description of the media.  
  - **`thumbnail`** *(optional, for videos)* : URL of a preview image for the video.  
- **`source`** : Object containing the news source details:  
  - **`name`** : Name of the news source.  
  - **`url`** : Link to the original news source.  
- **`timestamp`** : Time when the news was published.  
- **`disaster_type`** : Type of disaster (e.g., Flood, Earthquake, Wildfire).  
- **`location`** : Stores the location where the disaster occurred:
  - **`country`** : Country name.  
  - **`city`** : City name.  

---
