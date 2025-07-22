import * as React from 'react';
import Box from '@mui/material/Box';
import Typography from '@mui/material/Typography';
import {createTheme} from '@mui/material/styles';
import DashboardIcon from '@mui/icons-material/Dashboard';
import CommuteIcon from '@mui/icons-material/Commute';
import {AppProvider, type Navigation} from '@toolpad/core/AppProvider';
import {DashboardLayout} from '@toolpad/core/DashboardLayout';
import {useDemoRouter} from '@toolpad/core/internal';
import UpcomingTripsDashboard from "../trip/UpcomingTripsDashboard";



const NAVIGATION: Navigation = [
    {
        segment: 'dashboard',
        title: 'Dashboard',
        icon: <DashboardIcon/>,
    },
    {
        segment: 'upcoming-trips',
        title: 'Upcoming Trips',
        icon: <CommuteIcon/>,
    }
];

const theme = createTheme({
    cssVariables: {
        colorSchemeSelector: 'data-toolpad-color-scheme',
    },
    colorSchemes: {light: true, dark: true},
    breakpoints: {
        values: {
            xs: 0,
            sm: 600,
            md: 600,
            lg: 1200,
            xl: 1536,
        },
    },
});

function KindoDashboardPageContent({pathname}: { pathname: string }) {
    switch (pathname) {
        case '/upcoming-trips':
            return <UpcomingTripsDashboard/>;
        case '/dashboard':
            return (
                <Box
                    sx={{
                        py: 4,
                        display: 'flex',
                        flexDirection: 'column',
                        alignItems: 'center',
                        textAlign: 'center'
                    }}
                >
                    <Typography>Welcome to Kindo Challenge. Please navigate to the Upcoming Trips</Typography>
                </Box>
            );
        default:
            return <Typography>Page Not Found</Typography>;
    }
}


export default function DashboardLayoutBasic() {

    const router = useDemoRouter('/dashboard');


    return (
        <AppProvider
            navigation={NAVIGATION}
            router={router}
            theme={theme}
        >
            <DashboardLayout>
                <KindoDashboardPageContent pathname={router.pathname}/>
            </DashboardLayout>
        </AppProvider>
    );
}
