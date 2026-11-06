# AgroRent - Tractor & Farm Equipment Rental Platform

AgroRent is a modern, premium-quality, visually attractive, and fully responsive web platform designed specifically for renting tractors, combine harvesters, rotavators, seed drills, and agricultural machinery.

---

## 🌟 Key Features

1. **Exactly 10 Core Pages**:
   - `index.html` (Home Page 1: Tractor & Machinery Landing Page)
   - `home-2.html` (Home Page 2: Seasonal Offers & Popular Equipment)
   - `about.html` (About Us: Company Story, Mission, Vision, Fleet Standards & Team)
   - `equipment.html` (Complete 11-Category Machinery Catalog with Live Search & Filters)
   - `equipment-details.html` (Technical Specifications, Multi-Image Gallery, Hourly/Daily Rates)
   - `rates-pricing.html` (Comprehensive Pricing Matrix in Indian Rupees ₹, Operator & Transit Fees)
   - `booking.html` (Interactive Booking Engine with Real-Time Cost Calculation)
   - `farmer-dashboard.html` (Farmer Account Portal with 5 Metrics, Live Rentals, Bills & Invoices)
   - `login-register.html` (Farmer Authentication with 1-Click Demo Login & Password Toggle)
   - `contact.html` (Farmer Helpdesk, Inquiry Form, Depot Location & FAQ)

2. **UI & Design System**:
   - **Agricultural Color Palette**:
     - Deep Forest Green: `#173D2B`
     - Agricultural Green: `#347A45`
     - Fresh Green: `#78A85A`
     - Cream: `#F5F3E9`
     - Earth Brown: `#8B6746`
     - Dark Charcoal: `#202820`
     - Golden Yellow: `#E6AD43`
     - Pure White: `#FFFFFF`
   - **Typography**: Google Fonts Poppins, Inter, and Manrope.
   - **CSS Framework**: Tailwind CSS + Custom CSS Modules.

3. **Light Mode & Dark Mode**:
   - Toggle button on every page with smooth transitions and persistent state via `localStorage`.

4. **Bidirectional Layout (LTR / RTL Support)**:
   - Full English (LTR) and Arabic/Hebrew (RTL) toggle on every page.

5. **100% Relevant Agricultural Imagery**:
   - Genuine high-resolution images of tractors, harvesters, rotavators, seed drills, plowing fields, and farmers working across Indian farmland.

6. **Farmer Dashboard & Booking Persistence**:
   - Real-time booking form saves reservations into `localStorage`.
   - Dynamic calculation of days, operator charges, transport fees, and refundable deposit.
   - Unique Booking ID generation (e.g. `TR-849201`).
   - Printable and downloadable GST-compliant Tax Invoices via `window.print()`.

---

## 📁 Directory Structure

```text
Tractor-Farm-Equipment-Rental/
│
├── index.html
├── home-2.html
├── about.html
├── equipment.html
├── equipment-details.html
├── rates-pricing.html
├── booking.html
├── farmer-dashboard.html
├── login-register.html
├── contact.html
│
├── assets/
│   ├── images/
│   │   ├── home-1/
│   │   ├── home-2/
│   │   ├── about/
│   │   ├── equipment/
│   │   ├── equipment-details/
│   │   ├── pricing/
│   │   ├── booking/
│   │   ├── dashboard/
│   │   └── contact/
│   ├── icons/
│   └── fonts/
│
├── css/
│   ├── style.css
│   ├── responsive.css
│   ├── animations.css
│   ├── dark-mode.css
│   ├── rtl.css
│   └── pages/
│       ├── home-1.css
│       ├── home-2.css
│       ├── about.css
│       ├── equipment.css
│       ├── equipment-details.css
│       ├── pricing.css
│       ├── booking.css
│       ├── dashboard.css
│       ├── login-register.css
│       └── contact.css
│
├── js/
│   ├── main.js
│   ├── navigation.js
│   ├── theme.js
│   ├── rtl.js
│   ├── animations.js
│   ├── equipment.js
│   ├── equipment-details.js
│   ├── pricing.js
│   ├── booking.js
│   ├── auth.js
│   ├── dashboard.js
│   └── invoice.js
│
└── README.md
```

---

## 🚀 How to Run the Website

Simply open `index.html` in any modern web browser, or serve it using any local HTTP server:

```powershell
# Using Python
python -m http.server 8000

# Or using Node.js npx serve
npx serve .
```

Then visit `http://localhost:8000`.

---

## 🌾 Demo Farmer Credentials

- **Email**: `farmer@agrorent.in`
- **Password**: `farmer123`
- Or click the **"1-Click Login as Rajesh Kumar"** button on `login-register.html` for instant testing.
