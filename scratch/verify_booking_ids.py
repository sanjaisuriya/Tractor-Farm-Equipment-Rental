with open('booking.html', 'r', encoding='utf-8') as f:
    html = f.read()

expected_ids = ['sumEquipName', 'sumEquipCost', 'confirmBookingId', 'sumRatePerDay', 'sumDeposit', 'bookingStartDate', 'confirmDates', 'bookingEquipment', 'sumDeliveryCost', 'bookingDelivery', 'bookingCategory', 'bookingFarmerName', 'confirmFarmer', 'sumDuration', 'confirmTotal', 'bookingOperator', 'bookingEmail', 'bookingLocation', 'sumOperatorCost', 'confirmEquipName', 'bookingConfirmModal', 'bookingMobile', 'bookingEndDate', 'bookingNotes', 'sumTotalAmount', 'equipmentBookingForm']

missing = [i for i in expected_ids if f'id="{i}"' not in html]
print("Missing IDs:", missing)
