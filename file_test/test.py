from odoo import fields, models, api
from odoo.exceptions import ValidationError
from datetime import timedelta

    
    @api.constrains('booking_date', 'booking_time')
    def _check_booking_conflict(self):
        for record in self:
            if record.booking_date and record.booking_time:
                conflicting_bookings = self.env['pet.caretaker.booking'].search([
                    ('id', '!=', record.id),  # Không lấy bản ghi hiện tại
                    ('booking_date', '=', record.booking_date),  # Trùng ngày
                    ('status_booking', '!=', 'confirmed'),  # Chỉ tìm booking chưa xác nhận
                    ('booking_time', '>', record.booking_time + timedelta(hours=4)),  # Trước thời gian + 4h
                    ('booking_time', '>', record.booking_time)  # Đặt trong khoảng thời gian hợp lệ
                ])
                if conflicting_bookings:
                    raise ValidationError("This time slot is already booked on the selected date. Please choose another time.")
    
    