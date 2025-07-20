import axios from "axios";
import {FullFormData} from "../types";

class RegistrationService {
    saveRegisterByParentForm = async (registration: any) => {
        const {data: response} = await axios.post('/kindo/api/v1/form/register-by-parent/save', registration);
        return response;
    }
    saveRegistrationWithPayment = async (registrationWithPayment: FullFormData) => {
        const {data: response} = await axios.post('/kindo/api/v1/form/register-with-payment', registrationWithPayment);
        return response;
    }
}

// eslint-disable-next-line import/no-anonymous-default-export
export default new RegistrationService();