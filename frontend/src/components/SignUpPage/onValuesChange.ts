import type { SignUpPageProps } from '@/types/SignUpProps'

/**
 * onValuesChange is a callback function that is called when the form values change.
 * 
 * @param changedValues values that have changed, not used here
 * @param allValues all values of the form
 * @param setIsDisabled function to set the disabled state of the submit button, used in tests
 */
export const onValuesChange = (_changedValues: undefined, allValues: SignUpPageProps, setIsDisabled: (disabled: boolean) => void) => {
    // Check if all required fields are filled and if the password and confirm password match to enable the submit button
    if (
        allValues.username 
        && allValues.email 
        && allValues.rgpd 
        && allValues.rgpd 
        && allValues.confirmPassword 
        && allValues.confirmPassword === allValues.password 
        && allValues.password
    ) {
        setIsDisabled(false);
    } else {
        setIsDisabled(true);
    }
};