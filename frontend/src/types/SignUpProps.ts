/**
 * @SignUpPageProps is a TypeScript interface that defines the structure of the props
 * It is used to type the form values in the SignUpPage component.
 */
export type SignUpPageProps = {
    username: string;
    email: string;
    password: string;
    confirmPassword: string;
    rgpd: boolean;
};