import * as React from 'react';
import Typography from "@mui/material/Typography";
import Box from "@mui/material/Box";
import TripDataGrid from "./TripDataGrid";
import RegisterByParentForm from "../registration/RegisterByParentForm";
import OnlinePaymentForm from "../payment/OnlinePaymentForm";
import {FullFormData, Payment, Registration, School, TripDetail} from "../types";
import RegistrationService from "../services/RegistrationService";
import PaymentSuccessModal from "../payment/PaymentSuccessModal";
import PaymentUnsuccessModal from "../payment/PaymentUnsuccessModal";


export default function UpcomingTripsDashboard() {
    const [step, setStep] = React.useState(0);
    const [selectedRow, setSelectedRow] = React.useState<TripDetail>();
    const [school, setSchool] = React.useState<School>();
    const [registrationData, setRegistrationData] = React.useState<Registration>();
    const [showLoader, setShowLoader] = React.useState(false);
    const [paymentSuccess, setPaymentSuccess] = React.useState(false);
    const [paymentUnSuccess, setPaymentUnSuccess] = React.useState(false);

    const handleRegister = (row: any): any => {
        setStep(1);
        setSelectedRow(row)
    };
    const onSubmit = (regData: Registration) => {
        regData.tripdetail_id = selectedRow?.id as number
        setRegistrationData(regData)
        setSchool(selectedRow?.school)
        setStep(2);
    }

    const onPay = (payData: Payment) => {
        setShowLoader(true)
        payData.amount = selectedRow?.cost as number
        payData.card_number = payData.card_number.replace(/\s+/g, '')
        const fullFormData: FullFormData = {
            payment: payData,
            registration: registrationData!,
            school: school!
        };
        RegistrationService.saveRegistrationWithPayment(fullFormData).then((response) => {
            if (response.success) {
                setPaymentSuccess(true)
                setShowLoader(false)
            } else {
                setPaymentUnSuccess(true)
                setShowLoader(false)
                console.log("No rows found in getAllTripDetails!")
            }
        }).catch((ex) => {
            setShowLoader(false)
            console.log("Error in getAllTripDetails")
            console.log(ex)
        });
    }

    return (
        paymentSuccess ? <PaymentSuccessModal open={paymentSuccess} onClose={() => setPaymentSuccess(false)}
                                              setStep={() => setStep(0)}/> :
            paymentUnSuccess ? <PaymentUnsuccessModal open={paymentUnSuccess} onClose={() => setPaymentUnSuccess(false)}/> :
            step === 1 ? <RegisterByParentForm onSubmit={onSubmit} setStep={() => setStep(0)}/> :
                step === 2 ?
                    <OnlinePaymentForm onPay={onPay} amount={selectedRow?.cost as number} showLoader={showLoader}/> :
                    <Box
                        sx={{
                            py: 4,
                            display: 'flex',
                            flexDirection: 'column',
                            alignItems: 'center',
                            textAlign: 'center',
                        }}
                    >
                        <Typography sx={{fontWeight: 'bold'}}>
                            If you would like your child to participate in the upcoming field trip, please review the
                            trip details below and click the Register button to complete the payment and registration
                            process.
                        </Typography>
                        <br/>
                        <TripDataGrid handleRegister={handleRegister}/>
                    </Box>
    );

}