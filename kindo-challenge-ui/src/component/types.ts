export interface TripDetail {
    id: number;
    trip_name: string;
    trip_location: string;
    school_name: string;
    grade: number;
    date: string;
    cost: number;
    school: School
}
export interface School {
    id: number;
    school_name: string;

}
export interface Registration {
    firstname: string;
    lastname: string;
    grade: number;
    parent_name: string;
    relationship: string;
    email: string;
    contact: string;
    school_id: number;
    tripdetail_id: number;
}

export interface Payment {
    card_name: string;
    card_number: string;
    expiry_date: string;
    cvv: string;
    amount: number;
    school_id: number;
    activity_id: number;
}

export interface FullFormData {
    registration: Registration;
    payment: Payment;
    school: School;
}