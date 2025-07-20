import React, {useState} from 'react';
import {Box, Breadcrumbs, Button, Link, Paper, TextField, Typography,} from '@mui/material';


export default function RegisterByParentForm({onSubmit, setStep}:any) {
    const [formData, setFormData] = useState({
        firstname: '',
        lastname: '',
        grade: '',
        parent_name: '',
        relationship: '',
        contact: '',
        email: ''
    });

    const [errors, setErrors] = useState<{ [key: string]: string }>({});

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | { name?: string; value: unknown }>) => {
        const {name, value} = e.target;
        setFormData((prev) => ({...prev, [name as string]: value}));
        setErrors((prev) => ({...prev, [name as string]: ''}));
    };

    const validate = () => {
        const newErrors: { [key: string]: string } = {};
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        Object.entries(formData).forEach(([key, value]) => {
            if (!value) newErrors[key] = 'This field is required';

            if(key === 'grade' && Number(value) > 13 ){
               newErrors[key] = 'Enter a valid grade';
            }
            if(key === 'email' && !regex.test(value)){
                newErrors[key] = 'Enter a valid email address';
            }
        });
        setErrors(newErrors);
        return Object.keys(newErrors).length === 0;
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (validate()) {
            onSubmit(formData);
        }
    };

    return (
        <>
            <br/>
            <Breadcrumbs aria-label="breadcrumb">
                <Link underline="hover" color="inherit" sx={{ cursor: 'pointer' }}  onClick={()=>setStep()}>
                    &nbsp;Upcoming trips
                </Link>
                <Typography sx={{color: 'text.primary'}}>Register</Typography>
            </Breadcrumbs>

            <Paper elevation={1} sx={{p: 6, minWidth: 500, maxWidth: 700, mx: 'auto'}}>
                <Typography variant="h5" gutterBottom>
                    Trip Registration
                </Typography>
                <Box component="form" onSubmit={handleSubmit} noValidate autoComplete="off"
                     sx={{display: 'flex', flexDirection: 'column', gap: 2}}>
                    <TextField
                        label="Student First Name"
                        name="firstname"
                        value={formData.firstname}
                        onChange={handleChange}
                        error={!!errors.firstname}
                        helperText={errors.firstname}
                    />
                    <TextField
                        label="Student Last Name"
                        name="lastname"
                        value={formData.lastname}
                        onChange={handleChange}
                        error={!!errors.lastname}
                        helperText={errors.lastname}
                    />
                    <TextField
                        label="Student Grade"
                        name="grade"
                        type="number"
                        value={formData.grade}
                        onChange={handleChange}
                        error={!!errors.grade}
                        helperText={errors.grade}
                    />
                    <TextField
                        label="Parent Name"
                        name="parent_name"
                        value={formData.parent_name}
                        onChange={handleChange}
                        error={!!errors.parent_name}
                        helperText={errors.parent_name}
                    />
                    <TextField
                        label="Relationship"
                        name="relationship"
                        value={formData.relationship}
                        onChange={handleChange}
                        error={!!errors.relationship}
                        helperText={errors.relationship}
                    />
                    <TextField
                        label="Contact Number"
                        name="contact"
                        value={formData.contact}
                        onChange={handleChange}
                        error={!!errors.contact}
                        helperText={errors.contact}
                    />
                    <TextField
                        label="Email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        error={!!errors.email}
                        helperText={errors.email}
                    />
                    <Button type="submit" variant="contained" color="primary">
                        Register
                    </Button>
                </Box>
            </Paper>
        </>
    );
}