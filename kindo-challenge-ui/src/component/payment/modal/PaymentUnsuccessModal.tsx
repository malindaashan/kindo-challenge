import React from 'react';
import {Box, Button, Modal, Typography} from '@mui/material';
import CancelIcon from '@mui/icons-material/Cancel';

interface PaymentUnSuccessModalProps {
    open: boolean;
    onClose?: () => void;
    setStep?: () => void;
}

const PaymentUnSuccessModal: React.FC<PaymentUnSuccessModalProps> = ({open, onClose, setStep}) => {

    const handleClose = () => {
        if (setStep) {
            setStep()
        }
        if (onClose) {
            onClose();
        }
    };

    return (
        <Modal open={open} onClose={handleClose}>
            <Box
                sx={{
                    position: 'absolute',
                    top: '50%',
                    left: '50%',
                    transform: 'translate(-50%, -50%)',
                    bgcolor: 'white',
                    borderRadius: 2,
                    boxShadow: 24,
                    p: 4,
                    width: 300,
                    textAlign: 'center',
                }}
            >
                <Typography variant="h6" gutterBottom>
                    <CancelIcon/> Transaction Unsuccessful!
                </Typography>
                <Typography variant="body2" sx={{mb: 2}}>
                    Your payment is not successful. Please try again.
                </Typography>
                <Button variant="contained" color="primary" onClick={handleClose}>
                    Go to Dashboard
                </Button>
            </Box>
        </Modal>
    );
};

export default PaymentUnSuccessModal;