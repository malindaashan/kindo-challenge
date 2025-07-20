import React, {useState} from 'react';
import {Box, Button, Grid, Paper, TextField, Typography,} from '@mui/material';
import Loader from "../loader/Loader";

export default function OnlinePaymentForm({onPay, amount, showLoader}: any) {
    const [formData, setFormData] = useState({
        card_name: '',
        card_number: '',
        expiry_date: '',
        cvv: '',
    });

    const [errors, setErrors] = useState<{ [key: string]: string }>({});

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const {name, value} = e.target;
        let formattedValue = value;
        if (name === "card_number") {
            const digitsOnly = value.replace(/\D/g, '');
            formattedValue = digitsOnly.replace(/(.{4})/g, '$1 ').trim();
        }
        setFormData((prev) => ({...prev, [name]: formattedValue}));
        setErrors((prev) => ({...prev, [name]: ''}));
    };

    const validate = () => {
        const newErrors: { [key: string]: string } = {};
        Object.entries(formData).forEach(([key, value]) => {
            if (!value) newErrors[key] = 'This field is required';
        });

        if (formData.card_number && !/^\d{16}$/.test(formData.card_number.replace(/\s+/g, ''))) {
            newErrors.card_number = 'Card number must be 16 digits';
        }
        if (formData.expiry_date && !isValidExpiryDate(formData.expiry_date)) {
            newErrors.expiry_date = 'Expiry date is invalid';
        }

        if (formData.cvv && !/^\d{3}$/.test(formData.cvv)) {
            newErrors.cvv = 'CVV must be 3 digit';
        }
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };
    function isValidExpiryDate(expiry: string): boolean {
        // Check format MM/YY
        const regex = /^(0[1-9]|1[0-2])\/\d{2}$/;
        if (!regex.test(expiry)) return false;

        const [monthStr, yearStr] = expiry.split('/');
        const month = parseInt(monthStr, 10);
        const year = parseInt('20' + yearStr, 10); // convert to 4-digit year

        const now = new Date();
        const currentMonth = now.getMonth() + 1;
        const currentYear = now.getFullYear();

        // Check if expired
        return year > currentYear || (year === currentYear && month >= currentMonth);
    }

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (validate()) {
            onPay(formData);
        }
    };

    return (
        <>
            {showLoader ? <Loader/> :
                <Paper elevation={3} sx={{p: 4, maxWidth: 600, mx: 'auto'}}>
                    <Typography variant="h6" gutterBottom color="text.secondary">
                        Pay Amount <strong>${amount} NZD</strong>
                    </Typography>

                    <Box
                        component="form"
                        onSubmit={handleSubmit}
                        sx={{mt: 2}}
                        noValidate
                        autoComplete="off"
                    >
                        <Grid container spacing={2}>
                            <Grid>
                                <TextField
                                    fullWidth
                                    label="Name on Card"
                                    name="card_name"
                                    value={formData.card_name}
                                    onChange={handleChange}
                                    error={!!errors.card_name}
                                    helperText={errors.card_name}
                                />
                            </Grid>
                            <Grid>
                                <TextField
                                    fullWidth
                                    label="Card Number"
                                    name="card_number"
                                    value={formData.card_number}
                                    onChange={handleChange}
                                    error={!!errors.card_number}
                                    helperText={errors.card_number}
                                    inputProps={{maxLength: 19}}
                                />
                            </Grid>
                            <Grid>
                                <TextField
                                    fullWidth
                                    label="Expiry Date (MM/YY)"
                                    name="expiry_date"
                                    value={formData.expiry_date}
                                    onChange={handleChange}
                                    error={!!errors.expiry_date}
                                    helperText={errors.expiry_date}
                                />
                            </Grid>
                            <Grid>
                                <TextField
                                    fullWidth
                                    label="CVV"
                                    name="cvv"
                                    value={formData.cvv}
                                    onChange={handleChange}
                                    error={!!errors.cvv}
                                    helperText={errors.cvv}
                                    inputProps={{maxLength: 3}}
                                />
                            </Grid>
                        </Grid>
                        <Button
                            type="submit"
                            variant="contained"
                            color="primary"
                            sx={{mt: 3}}
                            fullWidth
                        >
                            Pay Now
                        </Button>
                    </Box>
                </Paper>
            }
        </>
    );
}