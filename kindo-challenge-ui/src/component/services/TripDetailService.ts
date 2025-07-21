import axios from "axios";

class TripDetailService {
    getAllTripDetails = async () => {
        const {data: response} = await axios.get('/kindo/api/v1/trip-details/get-all?page=1&limit=100');
        return response;
    }
}

// eslint-disable-next-line import/no-anonymous-default-export
export default new TripDetailService();