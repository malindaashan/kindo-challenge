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
        setFormData((prev) => ({...prev, [name]: value}));
        setErrors((prev) => ({...prev, [name]: ''}));
    };

    const validate = () => {
        const newErrors: { [key: string]: string } = {};
        Object.entries(formData).forEach(([key, value]) => {
            if (!value) newErrors[key] = 'This field is required';
        });

        if (formData.card_number && !/^\d{16}$/.test(formData.card_number)) {
            newErrors.cardNumber = 'Card number must be 16 digits';
        }

        if (formData.cvv && !/^\d{3,4}$/.test(formData.cvv)) {
            newErrors.cvv = 'CVV must be 3 or 4 digits';
        }

        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        alert(validate())
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
                                    inputProps={{maxLength: 16}}
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
                                    inputProps={{maxLength: 4}}
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