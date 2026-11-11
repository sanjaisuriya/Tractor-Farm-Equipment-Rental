/**
 * Tractor & Farm Equipment Rental - Equipment Catalog & Data Service
 * Comprehensive dataset covering all 6 core agricultural machinery categories:
 * 1. Tractors (Utility Tractors, Mini Tractors, Heavy-Duty Tractors, 4WD Tractors)
 * 2. Tillage Equipment (Rotavators, Cultivators, Disc Harrows, Ploughs)
 * 3. Sowing Equipment (Seed Drills, Planters, Seeders)
 * 4. Spraying Equipment (Boom Sprayers, Power Sprayers, Tractor Mounted Sprayers)
 * 5. Harvesting Equipment (Combine Harvesters, Reapers, Hay Balers)
 * 6. Transport Equipment (Tractor Trailers and Agricultural Transport Equipment)
 */

const EQUIPMENT_DATA = [
  // ==========================================
  // 1. TRACTORS
  // ==========================================
  {
    id: "tr-575",
    name: "Mahindra 575 DI High-Power Tractor",
    category: "Tractors",
    subCategory: "Utility Tractors",
    hp: "45 HP",
    hpNum: 45,
    engine: "4 Cylinder, 2730 CC MDI Diesel Engine",
    fuelType: "Diesel (Low Consumption)",
    workingCapacity: "Suitable for 2-3 Acres / hour ploughing",
    hourlyRate: 500,
    dailyRate: 3500,
    weeklyRate: 21000,
    monthlyRate: 75000,
    operatorRate: 700,
    transportRate: 30,
    status: "Available",
    rating: 4.9,
    reviewsCount: 142,
    image: "assets/images/equipment/mahindra-575-di.jpg",
    gallery: [
      "assets/images/equipment/mahindra-575-di.jpg",
      "assets/images/equipment/tractor.jpg",
      "assets/images/equipment-details/gallery-1.jpg"
    ],
    shortDesc: "Workhorse 45 HP multi-purpose utility tractor engineered for heavy ploughing, puddling, and haulage across all soil types.",
    description: "The Mahindra 575 DI is renowned among Indian farmers for fuel-efficient power, rugged build quality, and unmatched field versatility. Perfectly paired with 7-9 tine cultivators, rotavators, and heavy-duty trailers. Features high torque backup to handle sudden load shocks effortlessly.",
    features: [
      "Advanced 4-Cylinder Fuel-Efficient Engine",
      "Dual-acting Power Steering for fatigue-free operation",
      "Heavy-duty 1,600 kg Hydraulic Lift Capacity",
      "Oil-immersed Multi-disc Brakes for safety on slopes",
      "Partial Constant Mesh Transmission with 8F + 2R gears"
    ],
    specs: {
      "Engine Power": "45 HP @ 1900 RPM",
      "Displacement": "2730 CC, 4-Cylinder",
      "PTO Power": "39.8 HP (540 RPM)",
      "Hydraulic Lift": "1600 kg with High-Precision Depth Control",
      "Fuel Tank": "47 Liters Diesel Capacity",
      "Brakes": "Oil Immersed Multi-disc"
    }
  },
  {
    id: "tr-johndeere",
    name: "John Deere 5310 PowerTech 4WD Tractor",
    category: "Tractors",
    subCategory: "4WD Tractors",
    hp: "55 HP",
    hpNum: 55,
    engine: "3 Cylinder Turbocharged PowerTech Diesel",
    fuelType: "Diesel (Common Rail High Pressure)",
    workingCapacity: "Heavy deep tillage & 3-4 Acres / hour harrowing",
    hourlyRate: 650,
    dailyRate: 4500,
    weeklyRate: 27000,
    monthlyRate: 95000,
    operatorRate: 750,
    transportRate: 35,
    status: "Available",
    rating: 4.9,
    reviewsCount: 98,
    image: "assets/images/equipment/john-deere-5310.jpg",
    gallery: [
      "assets/images/equipment/john-deere-5310.jpg",
      "assets/images/home-1/hero-tractor.jpg",
      "assets/images/equipment-details/gallery-1.jpg"
    ],
    shortDesc: "Premium 55 HP four-wheel drive tractor with turbocharger, Collarshift gearbox, and heavy pull traction in wet clay.",
    description: "Built for progressive farmers operating laser levellers, large reversible MB ploughs, and heavy seeders. The 4WD system eliminates wheel slip in submerged paddy fields and black cotton soil, saving up to 25% on fuel and field time.",
    features: [
      "Turbocharged 55 HP PowerTech Engine with Piston Cooling Jets",
      "Mechanical Front Wheel Drive (4WD) with limited slip differential",
      "Dual Clutch with Independent PTO Lever",
      "2,000 kg Heavy-Duty Category II Hydraulic Lift",
      "Tilt & Telescopic Power Steering with ROPS Canopy"
    ],
    specs: {
      "Engine Power": "55 HP @ 2400 RPM Turbocharged",
      "Drive Type": "4-Wheel Drive (4WD)",
      "Transmission": "9 Forward + 3 Reverse Collarshift",
      "PTO Speed": "Dual Speed 540 & 540E Economy PTO",
      "Hydraulic Lift": "2000 kg Lift Capacity",
      "Fuel Tank": "68 Liters with Water Separator"
    }
  },
  {
    id: "mini-245",
    name: "Sonalika GT 22 Orchard Mini Tractor",
    category: "Tractors",
    subCategory: "Mini Tractors",
    hp: "22 HP",
    hpNum: 22,
    engine: "3 Cylinder Water-Cooled Fuel-Saver Diesel",
    fuelType: "Diesel (Ultra-Low Consumption)",
    workingCapacity: "Inter-row cultivation & 1-1.5 Acres / hr spraying",
    hourlyRate: 350,
    dailyRate: 2200,
    weeklyRate: 13000,
    monthlyRate: 48000,
    operatorRate: 600,
    transportRate: 25,
    status: "Available",
    rating: 4.8,
    reviewsCount: 76,
    image: "assets/images/equipment/sonalika-gt22-mini.jpg",
    gallery: [
      "assets/images/equipment/sonalika-gt22-mini.jpg",
      "assets/images/equipment/sonalika-gt22-mini-side.jpg",
      "assets/images/equipment/mini-tractor.jpg"
    ],
    shortDesc: "Narrow track 22 HP mini tractor designed specifically for vineyard lanes, sugarcane beds, and fruit orchards.",
    description: "Compact 3-foot track width enables effortless inter-row weeding, rotavating, and power spraying between tightly spaced crops. Offers smooth turning radius and featherweight ground pressure to protect delicate crop root zones.",
    features: [
      "Compact Narrow Track (under 3.2 feet overall width)",
      "Water-cooled 3-Cylinder High Fuel Efficiency Engine",
      "650 kg Precision 3-Point Hydraulic Linkage",
      "Tight 2.2 Meter Turning Radius for headlands",
      "Ergonomic low center-of-gravity anti-rollover chassis"
    ],
    specs: {
      "Engine Power": "22 HP @ 2700 RPM",
      "Overall Width": "940 mm (Super Narrow Track)",
      "Transmission": "6 Forward + 2 Reverse Sliding Mesh",
      "PTO Speed": "Multi-Speed PTO (540 & 1000 RPM)",
      "Hydraulics": "650 kg Automatic Draft & Position Control",
      "Ground Clearance": "210 mm"
    }
  },
  {
    id: "tr-swaraj855",
    name: "Swaraj 855 FE Heavy-Duty Farm Tractor",
    category: "Tractors",
    subCategory: "Heavy-Duty Tractors",
    hp: "52 HP",
    hpNum: 52,
    engine: "3 Cylinder, 3307 CC High-Torque Diesel",
    fuelType: "Diesel (High Torque Backup)",
    workingCapacity: "Heavy continuous tillage & threshing",
    hourlyRate: 580,
    dailyRate: 4000,
    weeklyRate: 24000,
    monthlyRate: 85000,
    operatorRate: 700,
    transportRate: 30,
    status: "In-Use",
    rating: 4.8,
    reviewsCount: 110,
    image: "assets/images/about/hero-tractor.jpg",
    gallery: [
      "assets/images/about/hero-tractor.jpg",
      "assets/images/equipment/tractor.jpg"
    ],
    shortDesc: "Legendary 52 HP heavy-duty agricultural tractor featuring high displacement for relentless pull in hard soil.",
    description: "The Swaraj 855 FE is engineered for demanding non-stop field work including deep ripping, laser levelling, and commercial threshing. Renowned for low operating temperatures and reliable mechanical toughness.",
    features: [
      "High Displacement 3307 CC Naturally Aspirated Engine",
      "Dual Clutch with Multispeed Reverse PTO",
      "1,700 kg Precision Hydraulic Lift",
      "Heavy Cast Front Axle for high stability with implements",
      "OIB Brakes and High Ground Clearance"
    ],
    specs: {
      "Engine Power": "52 HP @ 2000 RPM",
      "Displacement": "3307 CC, 3-Cylinder",
      "PTO Power": "42.9 HP with Multispeed PTO",
      "Hydraulics": "1700 kg Live Hydraulics with ADDC",
      "Clutch": "Heavy Duty Dual Clutch",
      "Steering": "Mechanical / Power Assisted"
    }
  },

  // ==========================================
  // 2. TILLAGE EQUIPMENT
  // ==========================================
  {
    id: "rot-48",
    name: "Shaktiman Semi-Champion 6 Feet Rotavator",
    category: "Tillage Equipment",
    subCategory: "Rotavators",
    hp: "Requires 40-50 HP Tractor",
    hpNum: 45,
    engine: "Tractor 540 RPM PTO Driven",
    fuelType: "PTO Powered",
    workingCapacity: "1.25 - 1.5 Acres / hour fine seedbed",
    hourlyRate: 250,
    dailyRate: 1600,
    weeklyRate: 9500,
    monthlyRate: 34000,
    operatorRate: 400,
    transportRate: 20,
    status: "Available",
    rating: 4.9,
    reviewsCount: 164,
    image: "assets/images/equipment/rotavator-tilling.jpg",
    gallery: [
      "assets/images/equipment/rotavator-tilling.jpg",
      "assets/images/equipment/rotavator.jpg"
    ],
    shortDesc: "Heavy-duty multi-speed rotary tiller with 48 boron steel L-blades for superior seedbed preparation and residue incorporation.",
    description: "The Shaktiman Semi-Champion rotavator pulverizes clods and chops standing crop stalks in a single pass. Features oil-bath multi-speed gearbox allowing rotor speed adjustments to match sandy, loamy, or heavy clay soil conditions.",
    features: [
      "48 Heavy-Duty Boron Steel Heat-Treated L-Type Blades",
      "Multi-Speed Gearbox (4 rotor speed combinations)",
      "Heavy-duty side gear drive in sealed oil bath",
      "Adjustable trailing board for leveled finish",
      "Shear bolt protected PTO propeller shaft"
    ],
    specs: {
      "Tillage Width": "1800 mm (6 Feet Working Width)",
      "Tractor Power Req": "40 to 50 HP with Cat-II 3-Point Hitch",
      "No. of Blades": "48 L-Type Blades (8 Flanges)",
      "Tillage Depth": "Up to 6 inches (150 mm)",
      "Total Weight": "440 kg",
      "Drive System": "Side Gear Drive with Multi-Speed Gearbox"
    }
  },
  {
    id: "cult-9",
    name: "Fieldking 9-Tyne Spring Loaded Cultivator",
    category: "Tillage Equipment",
    subCategory: "Cultivators",
    hp: "Requires 35-45 HP Tractor",
    hpNum: 40,
    engine: "Category-II 3-Point Linkage",
    fuelType: "Passive Draft Implement",
    workingCapacity: "2 - 2.5 Acres / hour secondary tillage",
    hourlyRate: 180,
    dailyRate: 1100,
    weeklyRate: 6500,
    monthlyRate: 22000,
    operatorRate: 350,
    transportRate: 20,
    status: "Available",
    rating: 4.7,
    reviewsCount: 89,
    image: "assets/images/equipment/cultivator.jpg",
    gallery: [
      "assets/images/equipment/cultivator.jpg",
      "assets/images/equipment-details/gallery-3.jpg"
    ],
    shortDesc: "Rugged 9-tyne cultivator with heavy tension springs for secondary tillage, aerating soil, and eradicating deep weed roots.",
    description: "Built with heavy channel frame and carbon-forged reversible shovels. Spring release mechanism automatically trips over hidden rocks or roots and resets immediately, preventing shank breakage and reducing tractor clutch stress.",
    features: [
      "9 High-Strength Carbon Steel Forged Reversible Shovels",
      "Dual Spring Loaded System for automatic obstacle tripping",
      "Heavy Seamless Channel Steel Box Frame",
      "Adjustable row-to-row spacing for custom tillage width",
      "Zero grease maintenance sealed pivot bushes"
    ],
    specs: {
      "Working Width": "2050 mm (6.7 Feet)",
      "No. of Tynes": "9 Spring Loaded Tynes",
      "Shovel Material": "Heat Treated High-Carbon Forged Steel",
      "Tractor Power Req": "35 to 45 HP",
      "Weight": "265 kg",
      "Linkage": "Cat-I & Cat-II Compatible"
    }
  },
  {
    id: "plough-mb3",
    name: "Lemken 3-Furrow Reversible MB Plough",
    category: "Tillage Equipment",
    subCategory: "Ploughs",
    hp: "Requires 50-65 HP Tractor",
    hpNum: 55,
    engine: "Dual-acting Hydraulic Turnover Cylinder",
    fuelType: "Hydraulic Powered Turnover",
    workingCapacity: "1 - 1.25 Acres / hour deep ploughing",
    hourlyRate: 300,
    dailyRate: 1900,
    weeklyRate: 11500,
    monthlyRate: 40000,
    operatorRate: 450,
    transportRate: 25,
    status: "Available",
    rating: 4.9,
    reviewsCount: 57,
    image: "assets/images/equipment/plough.jpg",
    gallery: [
      "assets/images/equipment/plough.jpg",
      "assets/images/equipment/rotavator.jpg"
    ],
    shortDesc: "Precision reversible hydraulic mouldboard plough for deep inverted soil furrowing and hardpan eradication.",
    description: "Engineered for deep soil inversion, burying weeds, stubble, and pests while bringing nutrient-rich subsoil to the top. The hydraulic 180° rollover flips plough bodies at field headlands, eliminating dead furrows and leaving an even surface.",
    features: [
      "Hydraulic In-Cab 180° Rollover Turnaround Mechanism",
      "Hardened Boron Steel Share Points and Mouldboards",
      "Shear Bolt Overload Protection on each body",
      "Adjustable Furrow Width (12 to 16 inches per furrow)",
      "Eliminates empty headland runs and ridge furrows"
    ],
    specs: {
      "No. of Furrows": "3 Bottom Reversible Bodies",
      "Working Depth": "Up to 12 inches (300 mm)",
      "Tractor Power Req": "50 to 65 HP with Dual Auxiliary Valves",
      "Total Weight": "520 kg",
      "Frame Material": "High-Tensile Micro-Alloy Steel",
      "Turnover": "Dual-Acting Hydraulic Ram"
    }
  },
  {
    id: "harrow-disc",
    name: "Heavy-Duty 16-Disc Trailed Offset Harrow",
    category: "Tillage Equipment",
    subCategory: "Disc Harrows",
    hp: "Requires 45-60 HP Tractor",
    hpNum: 50,
    engine: "Heavy High-Carbon Notched Steel Discs",
    fuelType: "Draft Implement",
    workingCapacity: "2 - 3 Acres / hour clod breaking",
    hourlyRate: 280,
    dailyRate: 1750,
    weeklyRate: 10500,
    monthlyRate: 36000,
    operatorRate: 400,
    transportRate: 25,
    status: "Available",
    rating: 4.8,
    reviewsCount: 63,
    image: "assets/images/about/mission-rotavator.jpg",
    gallery: [
      "assets/images/about/mission-rotavator.jpg",
      "assets/images/equipment/rotavator.jpg"
    ],
    shortDesc: "High-grade boron steel offset disc harrow for breaking clods, chopping dry crop stalks, and leveling rough fields.",
    description: "Designed for primary and secondary tillage in tough, dry, trashy fields. The front notched discs slice through hard stubble and dry roots while rear smooth discs pulverize clods and leave a uniform tilth.",
    features: [
      "16 High-Carbon Boron Steel Discs (Front Notched, Rear Plain)",
      "Heavy Cast Spools with Double Ball Bearings",
      "Adjustable Gang Angle for varied soil penetration depth",
      "Heavy Steel Box Tube Frame for natural ballast weight",
      "Scraper Blades on every disc to prevent clay clogging"
    ],
    specs: {
      "Number of Discs": "16 Discs (8 Front / 8 Rear)",
      "Disc Diameter": "20 inches (510 mm)",
      "Working Width": "1850 mm (6 Feet)",
      "Tractor Power Req": "45 to 60 HP",
      "Total Weight": "480 kg",
      "Bearing Type": "Heavy-Duty Sealed Grease Bearings"
    }
  },

  // ==========================================
  // 3. SOWING EQUIPMENT
  // ==========================================
  {
    id: "seed-super",
    name: "Dasmesh Happy Seeder & Zero-Till Seed Drill",
    category: "Sowing Equipment",
    subCategory: "Seed Drills",
    hp: "Requires 45-55 HP Tractor",
    hpNum: 50,
    engine: "Combined Flail Rotor & Inverted T-Boot Furrow Openers",
    fuelType: "PTO + 3-Point Linkage",
    workingCapacity: "1.25 - 1.5 Acres / hour zero-till planting",
    hourlyRate: 350,
    dailyRate: 2100,
    weeklyRate: 12500,
    monthlyRate: 44000,
    operatorRate: 450,
    transportRate: 25,
    status: "Available",
    rating: 4.9,
    reviewsCount: 118,
    image: "assets/images/equipment/seed-drill.jpg",
    gallery: [
      "assets/images/equipment/seed-drill.jpg",
      "assets/images/equipment-details/gallery-1.jpg"
    ],
    shortDesc: "Direct zero-till seed and fertilizer drill allowing planting wheat and pulses directly into heavy standing paddy stubble.",
    description: "The gold standard for eco-friendly zero-stubble-burning agriculture. The front flail rotor clears a clean narrow strip through heavy paddy straw while rear seed boots deposit seed and DAP fertilizer simultaneously with zero field burning.",
    features: [
      "Zero Stubble Burning — plants straight into heavy mulch",
      "Simultaneous Dual Fluted Seed & Fertilizer Metering Box",
      "Inverted T-Boot Openers for minimal soil moisture loss",
      "Press Wheels ensure positive seed-to-soil contact",
      "Saves ₹2,500/acre in preparatory tillage fuel costs"
    ],
    specs: {
      "No. of Rows": "9 to 11 Tynes (Row Spacing 200 mm)",
      "Tractor Power Req": "45 to 55 HP with Dual Clutch",
      "Hopper Capacity": "Seed 50 kg + Fertilizer 55 kg",
      "Drive System": "Rear Ground Wheel Chain Drive + PTO Flail",
      "Working Speed": "3.5 to 5.0 km/h",
      "Weight": "680 kg"
    }
  },
  {
    id: "seed-planter",
    name: "Multi-Crop Pneumatic Precision Seed Planter",
    category: "Sowing Equipment",
    subCategory: "Planters",
    hp: "Requires 40-50 HP Tractor",
    hpNum: 45,
    engine: "Vacuum Pneumatic Metering Unit with PTO Blower",
    fuelType: "PTO Driven Fan + Ground Metering",
    workingCapacity: "2 - 2.5 Acres / hour precision planting",
    hourlyRate: 380,
    dailyRate: 2400,
    weeklyRate: 14500,
    monthlyRate: 50000,
    operatorRate: 450,
    transportRate: 25,
    status: "Available",
    rating: 4.8,
    reviewsCount: 42,
    image: "assets/images/about/company-tractor.jpg",
    gallery: [
      "assets/images/about/company-tractor.jpg",
      "assets/images/equipment/seed-drill.jpg"
    ],
    shortDesc: "Accurate pneumatic single-seed metering planter for cotton, maize, groundnut, and sunflower with uniform depth control.",
    description: "Guarantees exact plant-to-plant and row-to-row spacing with zero seed cracking. Powerful vacuum fan holds individual seeds onto rotating discs, dropping them at calibrated intervals to maximize sunlight absorption and crop yield.",
    features: [
      "Individual Row Vacuum Metering Discs for diverse seed sizes",
      "Double Disc Furrow Openers with Depth Gauge Wheels",
      "Heavy-duty Rubber V-Press Wheels for optimal germination",
      "Independent Row Seed Hoppers with clear sight glasses",
      "Cuts seed wastage by up to 35% compared to manual broadcasting"
    ],
    specs: {
      "No. of Rows": "4 Rows (Adjustable 45 to 75 cm Spacing)",
      "Tractor Power Req": "40 to 50 HP with 540 RPM PTO",
      "Seed Types": "Maize, Cotton, Soybean, Groundnut, Sunflower",
      "Hopper Volume": "35 Liters per Row Unit",
      "Planting Depth": "Adjustable 2 to 8 cm",
      "Weight": "420 kg"
    }
  },
  {
    id: "paddy-transplant",
    name: "Automatic 4-Row Ride-On Paddy Seeder & Transplanter",
    category: "Sowing Equipment",
    subCategory: "Seeders",
    hp: "18 HP Self-Powered Diesel",
    hpNum: 18,
    engine: "Water-Cooled OHV Agri Diesel Engine",
    fuelType: "Diesel (Low 0.8 L/hr)",
    workingCapacity: "3 - 4 Acres / day flooded field planting",
    hourlyRate: 450,
    dailyRate: 3200,
    weeklyRate: 19000,
    monthlyRate: 68000,
    operatorRate: 600,
    transportRate: 30,
    status: "In-Use",
    rating: 4.8,
    reviewsCount: 39,
    image: "assets/images/home-2/popular-tractor.jpg",
    gallery: [
      "assets/images/home-2/popular-tractor.jpg",
      "assets/images/equipment/seed-drill.jpg"
    ],
    shortDesc: "High-efficiency mechanized rice seeder ensuring uniform hill-to-hill spacing and root-friendly paddy seedling placement.",
    description: "Transforms labour-intensive paddy transplantation into a swift, mechanized single-person operation. Navigates knee-deep muddy puddling with specialized rubber lugged paddy wheels without sinking.",
    features: [
      "Automated Nursery Mat Feeding and Needle Claw Insertion",
      "Adjustable Hills per Square Meter (14 to 28 hills)",
      "High-Flotation Large Lugged Mud-Terrain Paddy Wheels",
      "Hydraulic Auto-Leveling Sensor preserves planting depth",
      "Saves over 85% on manual labor transplant costs"
    ],
    specs: {
      "Rows Planted": "4 Rows Simultaneously (30 cm Spacing)",
      "Engine": "18 HP Water-Cooled Diesel Engine",
      "Hill Distance": "12, 14, 16, 18 cm (Selectable)",
      "Speed": "Up to 1.5 m/sec Working Speed",
      "Depth Control": "Hydraulic Floating Sensor",
      "Total Weight": "320 kg"
    }
  },

  // ==========================================
  // 4. SPRAYING EQUIPMENT
  // ==========================================
  {
    id: "spray-500",
    name: "Mitra 500L Tractor Mounted Orchard & Crop Sprayer",
    category: "Spraying Equipment",
    subCategory: "Tractor Mounted Sprayers",
    hp: "Requires 24-50 HP Tractor",
    hpNum: 30,
    engine: "PTO Driven 55 LPM Ceramic Piston Pump",
    fuelType: "PTO Powered",
    workingCapacity: "4 - 5 Acres / hour fine droplet coverage",
    hourlyRate: 280,
    dailyRate: 1800,
    weeklyRate: 10500,
    monthlyRate: 38000,
    operatorRate: 400,
    transportRate: 20,
    status: "Available",
    rating: 4.8,
    reviewsCount: 94,
    image: "assets/images/equipment/sprayer.jpg",
    gallery: [
      "assets/images/equipment/sprayer.jpg",
      "assets/images/about/vision-fleet.jpg"
    ],
    shortDesc: "Heavy chemical-resistant 500-liter polyethylene tank with aerodynamic fan delivering ultra-fine mist for orchards and tall crops.",
    description: "Engineered for high-velocity, uniform chemical misting across pomegranate, citrus, mango, cotton, and grape vineyards. Dual-speed gearbox powers an aerodynamic fan with brass anti-drip nozzles for 100% underside leaf coverage.",
    features: [
      "500-Liter UV-Stabilized Polyethylene Tank with Agitator",
      "Rear Aerodynamic High-Airflow Mist Blower Fan",
      "Italian High-Pressure Triple Ceramic Piston Pump",
      "Dual Filtration System eliminates nozzle blockages",
      "Brass Anti-Drip Ceramic Core Nozzles with individual shut-off"
    ],
    specs: {
      "Tank Capacity": "500 Liters with Integrated Fresh Water Tank",
      "Pump Pressure": "Up to 40 Bar (580 PSI) Working Pressure",
      "Pump Flow": "55 Liters / Minute Output",
      "Tractor Power Req": "24 to 50 HP (Fits Mini & Standard Tractors)",
      "Nozzle Count": "12 to 14 Dual Brass Nozzles",
      "Mounting": "Category-I & II 3-Point Linkage"
    }
  },
  {
    id: "spray-boom",
    name: "Hydraulic 40-Nozzle 12-Meter Folding Boom Sprayer",
    category: "Spraying Equipment",
    subCategory: "Boom Sprayers",
    hp: "Requires 35-50 HP Tractor",
    hpNum: 40,
    engine: "Diaphragm Pump & Tri-Jet Anti-Drip Nozzles",
    fuelType: "PTO Driven Diaphragm Pump",
    workingCapacity: "8 - 10 Acres / hour broad-acre spraying",
    hourlyRate: 320,
    dailyRate: 2000,
    weeklyRate: 12000,
    monthlyRate: 42000,
    operatorRate: 400,
    transportRate: 25,
    status: "Available",
    rating: 4.9,
    reviewsCount: 51,
    image: "assets/images/about/vision-fleet.jpg",
    gallery: [
      "assets/images/about/vision-fleet.jpg",
      "assets/images/equipment/sprayer.jpg"
    ],
    shortDesc: "Wide 12-meter hydraulic boom sprayer providing fast, wind-drift protected coverage for cotton, wheat, and sugarcane acreage.",
    description: "Covers expansive open crop acreage in record time. Features hydraulic boom lifting and fold-in wing arms with self-leveling pendulum suspension that absorbs tractor rocking on uneven furrows.",
    features: [
      "12-Meter Wing Span with Hydraulic Vertical Fold",
      "Self-Leveling Mechanical Pendulum Suspension",
      "Tri-Jet Turret Nozzles for instant spray pattern switching",
      "600-Liter Chemical Tank with Turbo Hydromixer",
      "Electronic In-Cab Pressure Regulation System"
    ],
    specs: {
      "Working Width": "12 Meters (40 Feet Boom Width)",
      "Tank Capacity": "600 Liters",
      "Nozzle Count": "40 Tri-Jet Ceramic Fan Nozzles",
      "Tractor Power Req": "35 to 50 HP",
      "Pump Type": "Heavy-Duty 4-Diaphragm Pump (80 L/min)",
      "Height Range": "0.5m to 1.8m Hydraulic Adjustment"
    }
  },
  {
    id: "spray-power",
    name: "High-Pressure HTP Orchard Power Sprayer",
    category: "Spraying Equipment",
    subCategory: "Power Sprayers",
    hp: "8 HP OHV Commercial Engine",
    hpNum: 8,
    engine: "Triple Stainless Steel Piston Pump",
    fuelType: "Petrol / Kerosene Dual Fuel",
    workingCapacity: "2 - 3 Acres / hour targeted spraying",
    hourlyRate: 200,
    dailyRate: 1200,
    weeklyRate: 7000,
    monthlyRate: 24000,
    operatorRate: 350,
    transportRate: 15,
    status: "Available",
    rating: 4.7,
    reviewsCount: 68,
    image: "assets/images/about/story-tractor.jpg",
    gallery: [
      "assets/images/about/story-tractor.jpg",
      "assets/images/equipment/sprayer.jpg"
    ],
    shortDesc: "Portable high-pressure power sprayer with 150m delivery hose for horticultural plantations, vegetable greenhouses, and pest control.",
    description: "Rugged skid-mounted high-pressure power sprayer powered by an 8 HP commercial petrol engine. Includes two 150-meter heavy-duty chemical hoses and brass spray guns for pinpoint spot application on tree canopies.",
    features: [
      "Heavy Triple Stainless Steel Plunger Pump delivering 50 Bar",
      "Comes with Two 150-Meter Braided High-Pressure Hoses",
      "Dual High-Atomization Adjustable Brass Turbo Spray Guns",
      "Skid-Mounted with Heavy Rubber Vibration Isolators",
      "Low Fuel Consumption (under 0.9 Liters per hour)"
    ],
    specs: {
      "Engine": "8 HP 4-Stroke Commercial OHV Engine",
      "Pump Output": "30 to 45 Liters / Minute",
      "Operating Pressure": "Up to 50 kg/cm² (700 PSI)",
      "Hose Length": "2 x 150 Meters Reels Included",
      "Weight": "62 kg (Easily portable by 2 persons)",
      "Fuel Tank": "3.6 Liters"
    }
  },

  // ==========================================
  // 5. HARVESTING EQUIPMENT
  // ==========================================
  {
    id: "harv-9000",
    name: "Preet 987 Self-Propelled Multi-Crop Combine Harvester",
    category: "Harvesting Equipment",
    subCategory: "Combine Harvesters",
    hp: "101 HP Turbo Diesel",
    hpNum: 101,
    engine: "6-Cylinder Heavy-Duty Agri Turbocharged Engine",
    fuelType: "Diesel (Commercial Grade)",
    workingCapacity: "3.5 - 4.5 Acres / hour full harvesting & threshing",
    hourlyRate: 2200,
    dailyRate: 14500,
    weeklyRate: 85000,
    monthlyRate: 290000,
    operatorRate: 1200,
    transportRate: 50,
    status: "Available",
    rating: 4.9,
    reviewsCount: 88,
    image: "assets/images/equipment/harvester.jpg",
    gallery: [
      "assets/images/equipment/harvester.jpg",
      "assets/images/home-2/rental-offers.jpg",
      "assets/images/home-2/equipment-rental.jpg"
    ],
    shortDesc: "Heavy-duty 14-foot cutter bar combine harvester offering clean threshing, minimal grain loss, and automatic grain tank unloading.",
    description: "India's premier self-propelled combine harvester for paddy, wheat, soybean, and mustard. Equipped with a heavy rasp-bar threshing drum, wide grain straw walkers, and high-speed unloading auger delivering 99.5% clean grain separation.",
    features: [
      "14-Foot Heavy Multi-Crop Floating Cutter Bar with Reel",
      "Large 2,400-Liter Grain Tank with High-Speed Discharge Auger",
      "Heavy 5-Straw Walker System ensures under 0.5% grain loss",
      "Power Steering and Air-Conditioned Panoramic Operator Cab",
      "Reinforced Paddy Track Wheels for slushy submerged fields"
    ],
    specs: {
      "Engine Power": "101 HP @ 2200 RPM, 6-Cylinder Turbo Diesel",
      "Cutter Bar Width": "14 Feet (4.27 Meters)",
      "Grain Tank": "2400 Liters Capacity",
      "Threshing Drum": "Rasp Bar Drum (Diameter 600 mm)",
      "Fuel Tank": "240 Liters Heavy Steel Tank",
      "Total Weight": "8,700 kg"
    }
  },
  {
    id: "reaper-bind",
    name: "Tractor-Mounted Multi-Crop Reaper Binder",
    category: "Harvesting Equipment",
    subCategory: "Reapers",
    hp: "Requires 35-50 HP Tractor",
    hpNum: 40,
    engine: "Front Tractor 3-Point Linkage with PTO Drive",
    fuelType: "PTO Powered",
    workingCapacity: "1 - 1.5 Acres / hour reaping and bundling",
    hourlyRate: 600,
    dailyRate: 3800,
    weeklyRate: 22000,
    monthlyRate: 78000,
    operatorRate: 500,
    transportRate: 30,
    status: "Available",
    rating: 4.8,
    reviewsCount: 47,
    image: "assets/images/home-2/rental-offers.jpg",
    gallery: [
      "assets/images/home-2/rental-offers.jpg",
      "assets/images/equipment/harvester.jpg"
    ],
    shortDesc: "Harvests and automatically bundles wheat, oats, and paddy stalks into neat sheaves in a single continuous pass.",
    description: "Reaps grain stalks 5 cm above ground level and automatically binds them with jute twine into firm, uniform bundles. Preserves 100% of the long straw for cattle feed while avoiding grain shattering in the field.",
    features: [
      "Simultaneous Cutting and Jute Twine Automatic Bundling",
      "Low Cutting Height (5 cm) maximizes fodder yield",
      "Heavy Serrated Knife Blades cut cleanly through thick crop stalks",
      "Conveyor Belt delivers sheaves gently without seed loss",
      "Replaces over 20 manual harvesters per day"
    ],
    specs: {
      "Working Width": "1200 mm (4 Feet)",
      "Tractor Power Req": "35 to 50 HP Tractor",
      "Crops Handled": "Wheat, Paddy, Oats, Barley",
      "Twine Type": "Biodegradable Jute or Poly Twine",
      "Binding Mechanism": "Mechanical Knotter Billhook",
      "Total Weight": "390 kg"
    }
  },
  {
    id: "baler-straw",
    name: "Heavy-Duty Round Straw & Fodder Hay Baler",
    category: "Harvesting Equipment",
    subCategory: "Hay Balers",
    hp: "Requires 45-60 HP Tractor",
    hpNum: 50,
    engine: "PTO Driven High-Density Hydraulic Compression",
    fuelType: "PTO Driven",
    workingCapacity: "50 - 70 Round Bales / hour",
    hourlyRate: 700,
    dailyRate: 4200,
    weeklyRate: 25000,
    monthlyRate: 88000,
    operatorRate: 500,
    transportRate: 30,
    status: "In-Use",
    rating: 4.9,
    reviewsCount: 54,
    image: "assets/images/home-2/equipment-rental.jpg",
    gallery: [
      "assets/images/home-2/equipment-rental.jpg",
      "assets/images/equipment/harvester.jpg"
    ],
    shortDesc: "Compresses post-harvest crop residue into compact weather-resistant round bales for livestock fodder and bio-fuel transport.",
    description: "The premier solution for post-harvest straw management. Collects loose wheat or paddy straw left by combines, compresses it tightly into compact round bales, and wraps them securely with twine for easy transport and moisture protection.",
    features: [
      "Wide Pickup Reel with Spring Steel Tines gathers all loose straw",
      "High-Compression Steel Roller Chamber for dense, compact bales",
      "Automatic Twine Wrapping System with in-cab acoustic buzzer",
      "Hydraulic Tailgate for fast, effortless bale ejection",
      "Enables profitable monetization of crop residue"
    ],
    specs: {
      "Bale Dimensions": "Diameter 50 cm x Width 70 cm (approx. 20-25 kg)",
      "Pickup Width": "800 mm Gathering Reel",
      "Tractor Power Req": "45 to 60 HP with 540 RPM PTO",
      "Capacity": "50 to 70 Bales per Hour",
      "Twine Type": "Hemp Twine or Net Wrap",
      "Total Weight": "540 kg"
    }
  },

  // ==========================================
  // 6. TRANSPORT EQUIPMENT
  // ==========================================
  {
    id: "trail-8t",
    name: "Heavy-Duty 8-Tonne Hydraulic Tipping Trailer",
    category: "Transport Equipment",
    subCategory: "Tractor Trailers",
    hp: "Requires 40+ HP Tractor",
    hpNum: 40,
    engine: "Multi-Stage Single-Acting Hydraulic Telescopic Ram",
    fuelType: "Hydraulic Powered Tipping",
    workingCapacity: "8 Tonnes Grain / Biomass / Sand Payload",
    hourlyRate: 220,
    dailyRate: 1500,
    weeklyRate: 8500,
    monthlyRate: 29000,
    operatorRate: 350,
    transportRate: 20,
    status: "Available",
    rating: 4.8,
    reviewsCount: 127,
    image: "assets/images/equipment/trailer.jpg",
    gallery: [
      "assets/images/equipment/trailer.jpg",
      "assets/images/booking/booking-banner.jpg"
    ],
    shortDesc: "Reinforced corrugated steel trolley with 3-way hydraulic tipping for fast mandi harvest transport, manure, and gravel haulage.",
    description: "Fabricated from heavy 10-gauge structural channel steel and reinforced corrugated side panels. Connected via tractor auxiliary hydraulic coupler for rapid 50° high-angle dumping of grain, sugarcane, sand, and farm manure.",
    features: [
      "8-Tonne Certified Structural Payload Capacity",
      "Multi-Stage Heavy-Duty Hard-Chromed Telescopic Hydraulic Ram",
      "Reinforced Leaf Spring Suspension absorbs rough field ruts",
      "Removable High-Stakes Side Panels for oversized sugarcane loads",
      "Reflector Tape, Safety Chains, and Air-Assisted Brake provision"
    ],
    specs: {
      "Payload Capacity": "8,000 kg (8 Tonnes)",
      "Bed Dimensions": "12 Feet Length x 6 Feet Width x 2.5 Feet Height",
      "Tipping Angle": "50 Degrees Hydraulic Tipping",
      "Axle": "Heavy Square Solid Axle with Tapered Roller Bearings",
      "Tires": "9.00 x 16 Heavy-Duty Agricultural Radial Tires",
      "Tractor Requirement": "40 HP or higher with Single Auxiliary Valve"
    }
  },
  {
    id: "trail-mandi",
    name: "Dual-Axle 12-Tonne Grain Haulage Mandi Trolley",
    category: "Transport Equipment",
    subCategory: "Agricultural Transport Equipment",
    hp: "Requires 50+ HP Tractor",
    hpNum: 50,
    engine: "Dual Heavy Axles with Agricultural Leaf Springs",
    fuelType: "Hydraulic Heavy Tip",
    workingCapacity: "12 Tonnes Bulk Grain / Sugarcane Haulage",
    hourlyRate: 300,
    dailyRate: 2100,
    weeklyRate: 12500,
    monthlyRate: 44000,
    operatorRate: 400,
    transportRate: 25,
    status: "Available",
    rating: 4.9,
    reviewsCount: 73,
    image: "assets/images/booking/booking-banner.jpg",
    gallery: [
      "assets/images/booking/booking-banner.jpg",
      "assets/images/equipment/trailer.jpg"
    ],
    shortDesc: "High-volume dual-axle grain trolley built for heavy long-distance Mandi haulage, sugarcane transit, and bulk grain bags.",
    description: "The ideal heavy transport trailer for large acreage harvests and long-distance Mandi trips. Dual-axle rocker beam tandem suspension distributes wheel weight evenly, preventing soil compaction and ensuring highway stability.",
    features: [
      "12-Tonne High-Volume Mandi Harvest Capacity",
      "Tandem Dual-Axle Rocker Beam Suspension for smooth highway towing",
      "Heavy 4-Stage Telescopic Cylinder with quick-release ISO coupling",
      "Grain-Tight Locking Tailgate with bottom grain discharge hatch",
      "High clearance drawbar with 360-degree swivel towing eye"
    ],
    specs: {
      "Payload Capacity": "12,000 kg (12 Tonnes)",
      "Bed Dimensions": "14 Feet Length x 7 Feet Width x 3 Feet Height",
      "Suspension": "Heavy Tandem Dual-Axle Multi-Leaf System",
      "Tipping System": "4-Stage Hard-Chromed Hydraulic Cylinder",
      "Tires": "4 x 10.00 x 20 Commercial Grade Nylon Ribbed Tires",
      "Tractor Requirement": "50 HP or higher"
    }
  },
  {
    id: "pump-10hp",
    name: "Kirloskar 10 HP High-Discharge Farm Irrigation Pump",
    category: "Transport Equipment",
    subCategory: "Agricultural Transport Equipment",
    hp: "10 HP High-Flow Diesel",
    hpNum: 10,
    engine: "Heavy-Duty Centrifugal High-Discharge Pump",
    fuelType: "Diesel (Low 1.1 L/hr)",
    workingCapacity: "1,800 Liters / Minute canal & flood irrigation",
    hourlyRate: 180,
    dailyRate: 1200,
    weeklyRate: 7000,
    monthlyRate: 24000,
    operatorRate: 300,
    transportRate: 15,
    status: "Available",
    rating: 4.7,
    reviewsCount: 92,
    image: "assets/images/equipment/water-pump.jpg",
    gallery: [
      "assets/images/equipment/water-pump.jpg",
      "assets/images/equipment/sprayer.jpg"
    ],
    shortDesc: "Rapid water transfer and flood dewatering agricultural pump delivering 1,800 LPM flow for canal and pond irrigation.",
    description: "Heavy-duty agricultural diesel water pump set mounted on a steel wheel-barrow frame with pneumatic wheels. Features self-priming high-head centrifugal impeller designed to handle silt and farm runoff without clogging.",
    features: [
      "High Discharge Volume (108,000 Liters per hour / 1,800 LPM)",
      "Mounted on Heavy Trolley Frame with Pneumatic Wheels for easy farm transit",
      "Fuel Efficient 10 HP Water-Cooled Single Cylinder Diesel Engine",
      "Includes 30 Feet Suction Hose + 100 Feet Heavy Delivery Hose",
      "Wear-resistant cast iron pump casing with replaceable wear plate"
    ],
    specs: {
      "Engine Power": "10 HP @ 1500 RPM, Direct Injection Diesel",
      "Discharge Rate": "1800 Liters / Minute (108 m³/hr)",
      "Suction x Delivery": "100 mm x 100 mm (4\" x 4\")",
      "Max Head": "24 Meters (80 Feet)",
      "Fuel Tank": "10 Liters (Up to 9 Hours continuous run)",
      "Total Weight": "135 kg"
    }
  }
];

// Service Object
const EquipmentService = {
  getAll() {
    return EQUIPMENT_DATA;
  },

  getById(id) {
    return EQUIPMENT_DATA.find(e => e.id === id) || EQUIPMENT_DATA[0];
  },

  getCategories() {
    return [
      "All Categories",
      "Tractors",
      "Tillage Equipment",
      "Sowing Equipment",
      "Spraying Equipment",
      "Harvesting Equipment",
      "Transport Equipment"
    ];
  },

  filter({ category, search, maxPrice, status, minHp }) {
    return EQUIPMENT_DATA.filter(item => {
      // Category filter (supports main category, subcategory, or legacy terms)
      if (category && category !== "All Categories") {
        const catNorm = category.toLowerCase().trim();
        const itemCat = item.category.toLowerCase().trim();
        const itemSub = (item.subCategory || "").toLowerCase().trim();
        
        // Exact category or subcategory match
        const matchesCat = itemCat === catNorm || itemSub === catNorm;
        // Legacy partial match (e.g. "Rotavators" or "Combine Harvesters")
        const matchesLegacy = itemCat.includes(catNorm) || itemSub.includes(catNorm) || item.name.toLowerCase().includes(catNorm);
        
        if (!matchesCat && !matchesLegacy) {
          return false;
        }
      }

      // Search keyword filter
      if (search && search.trim() !== '') {
        const query = search.toLowerCase().trim();
        const matchesName = item.name.toLowerCase().includes(query);
        const matchesCategory = item.category.toLowerCase().includes(query);
        const matchesSubCategory = (item.subCategory || "").toLowerCase().includes(query);
        const matchesDesc = item.shortDesc.toLowerCase().includes(query);
        const matchesHp = (item.hp || "").toLowerCase().includes(query);
        if (!matchesName && !matchesCategory && !matchesSubCategory && !matchesDesc && !matchesHp) {
          return false;
        }
      }

      // Price filter (dailyRate)
      if (maxPrice && item.dailyRate > maxPrice) {
        return false;
      }

      // Status filter
      if (status && status !== 'all') {
        const isMatch = item.status.toLowerCase() === status.toLowerCase();
        if (!isMatch) return false;
      }

      // HP filter
      if (minHp && item.hpNum < minHp) {
        return false;
      }

      return true;
    });
  },

  renderCard(item) {
    const isAvail = item.status === "Available";
    return `
      <div class="equipment-card group flex flex-col h-full bg-white dark:bg-[#1A261D] rounded-2xl overflow-hidden border border-gray-200 dark:border-gray-800 hover:shadow-xl transition-all duration-300">
        <!-- Card Image & Badges -->
        <div class="equipment-img-wrapper relative h-56 overflow-hidden bg-slate-100 dark:bg-slate-800">
          <img 
            src="${item.image}" 
            alt="${item.name}" 
            loading="lazy" 
            class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500"
            onerror="this.src='assets/images/equipment/tractor.jpg';"
          />
          <div class="absolute top-3 left-3 flex flex-wrap gap-1.5 z-10">
            <span class="badge-agri bg-white/95 dark:bg-[#173D2B]/95 text-forest dark:text-cream text-[11px] font-bold py-1 px-2.5 rounded-full shadow-sm backdrop-blur-sm border border-gray-200/50 dark:border-gray-700/50">
              ${item.category}
            </span>
            ${item.subCategory ? `
              <span class="badge-agri bg-forest/80 text-gold text-[10px] font-semibold py-1 px-2 rounded-full shadow-sm backdrop-blur-sm hidden sm:inline-block">
                ${item.subCategory}
              </span>
            ` : ''}
          </div>
          <div class="absolute top-3 right-3 z-10">
            <span class="badge-agri ${isAvail ? 'bg-emerald-600 text-white' : 'bg-amber-600 text-white'} text-[11px] font-bold py-1 px-2.5 rounded-full shadow-md flex items-center gap-1.5">
              <span class="w-1.5 h-1.5 rounded-full ${isAvail ? 'bg-emerald-200 animate-pulse' : 'bg-amber-200'}"></span>
              ${item.status}
            </span>
          </div>
        </div>

        <!-- Card Body -->
        <div class="p-5 flex-1 flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between text-xs text-muted mb-2">
              <span class="font-bold text-agri dark:text-fresh flex items-center gap-1">
                <i class="fa-solid fa-gauge-high"></i>
                <span>${item.hp}</span>
              </span>
              <span class="flex items-center text-amber-500 font-bold text-xs">
                <i class="fa-solid fa-star text-xs mr-1 text-gold"></i>
                <span>${item.rating}</span>
                <span class="text-muted ml-1 font-normal">(${item.reviewsCount})</span>
              </span>
            </div>

            <h3 class="font-bold text-base sm:text-lg text-slate-900 dark:text-white mb-2 leading-snug line-clamp-2 group-hover:text-agri transition-colors">
              ${item.name}
            </h3>

            <p class="text-xs sm:text-sm text-slate-600 dark:text-slate-300 mb-4 line-clamp-2 leading-relaxed">
              ${item.shortDesc}
            </p>
          </div>

          <!-- Card Rates & Action Buttons -->
          <div class="pt-3 border-t border-slate-100 dark:border-slate-800">
            <div class="flex items-baseline justify-between mb-4">
              <div>
                <span class="text-xl sm:text-2xl font-black text-agri dark:text-fresh font-heading">
                  ₹${item.dailyRate.toLocaleString('en-IN')}
                </span>
                <span class="text-xs text-muted font-medium">/ day</span>
              </div>
              <div class="text-right">
                <span class="text-xs sm:text-sm font-semibold text-slate-700 dark:text-slate-300">
                  ₹${item.hourlyRate}/hr
                </span>
              </div>
            </div>

            <div class="grid grid-cols-2 gap-2">
              <button 
                type="button" 
                class="view-details-btn btn-secondary text-xs py-2 px-2.5 justify-center rounded-xl font-bold flex items-center gap-1.5 hover:bg-slate-100 dark:hover:bg-slate-800 transition"
                data-id="${item.id}"
                aria-label="View specifications for ${item.name}"
              >
                <i class="fa-solid fa-eye text-agri"></i>
                <span>View Details</span>
              </button>
              <a 
                href="booking.html?id=${item.id}" 
                class="btn-primary text-xs py-2 px-2.5 justify-center rounded-xl font-bold flex items-center gap-1.5"
                aria-label="Book ${item.name} now"
              >
                <i class="fa-solid fa-calendar-check"></i>
                <span>Book Now</span>
              </a>
            </div>
          </div>
        </div>
      </div>
    `;
  }
};

window.EquipmentService = EquipmentService;
window.EQUIPMENT_DATA = EQUIPMENT_DATA;
